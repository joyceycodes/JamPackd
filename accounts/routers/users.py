from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    HTTPException,
    status,
)
from pydantic import BaseModel
from authenticator import authenticator
from jwtdown_fastapi.authentication import Token
from queries.users import (
    UserIn,
    UserOut,
    DuplicateAccountError,
    UserQueries,
)


router = APIRouter()


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: UserOut


class HttpError(BaseModel):
    detail: str


@router.get("/api/users/{user_id}", response_model=UserOut)
def get_user(
    email: str,
    response: Response,
    queries: UserQueries = Depends(),
):
    record = queries.get_user(email)
    print(record)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.post("/api/accounts", response_model=AccountToken | HttpError)
async def create_user(
    info: UserIn,
    request: Request,
    response: Response,
    accounts: UserQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = accounts.create_user(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.email, password=info.password)
    token = await authenticator.login(response, request, form, accounts)
    return AccountToken(account=account, **token.dict())


@router.delete("/api/users/{user_id}", response_model=bool)
def delete_user(user_id: str, queries: UserQueries = Depends()):
    queries.delete_user(user_id)
    return True
