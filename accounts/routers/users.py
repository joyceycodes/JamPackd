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
    username: str,
    response: Response,
    queries: UserQueries = Depends(),
):
    record = queries.get_user(username)
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
    print(info)
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = accounts.create_user(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.username, password=info.password)
    token = await authenticator.login(response, request, form, accounts)
    return AccountToken(account=account, **token.dict())


@router.delete("/api/accounts/{user_id}", response_model=bool)
def delete_user(user_id: str, queries: UserQueries = Depends()):
    queries.delete_user(user_id)
    return True


@router.get("/api/accounts/me/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: dict = Depends(authenticator.get_current_account_data),
) -> AccountToken | None:

    # example of when you might want authenticator.try_get_current_account_data
    # if account:
    #     # logged in response
    # else:
    #     # non logged in response

    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }
