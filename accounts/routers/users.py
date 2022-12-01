from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request,
    HTTPException,
    status,
)
from pydantic import BaseModel
from db import UserQueries
from authenticator import authenticator
from jwtdown_fastapi.authentication import Token
from db import (
    UsersOut,
    UserIn,
    UserOut,
    DuplicateAccountError,
    UserOutWithPassword,
)


router = APIRouter()


# class UserIn(BaseModel):
#     first: str
#     last: str
#     email: str
#     username: str
#     password: str


# class UserOut(BaseModel):
#     id: int | str
#     first: str
#     last: str
#     email: str
#     username: str


# class UsersOut(BaseModel):
#     users: list[UserOut]


# class UserOutWithPassword(UserOut):
#     hashed_password: str


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: UserOut


class HttpError(BaseModel):
    detail: str


# class UpdateUser(BaseModel):
#     first: str
#     last: str
#     email: EmailStr
#     username: str

#     class Config:
#         schema_extra = {
#             "example": {
#                 "first": "z",
#                 "last": "z",
#                 "email": "z@z.com",
#                 "username": "Z",
#             }
#         }


# def ResponseModel(data, message):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }


# def ErrorResponseModel(error, code, message):
#     return {"error": error, "code": code, "message": message}


@router.get("/api/users", response_model=UsersOut)
def users_list(queries: UserQueries = Depends()):
    return {
        "users": queries.get_all_users(),
    }


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


# @router.post("/api/users/", response_model=UserOut)
# def create_user(
#     user_in: UserIn,
#     queries: UserQueries = Depends(),
# ):
#     return queries.create_user(user_in)


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


# @router.put("/api/users/{user_id}", response_model=UserOut)
# async def update_user(id: str, req: UpdateUser = Body(...)):
#     req = {k: v for k, v in req if v is not None}
#     updated_user = update_user(id, req)
#     update_query = {
#         "$set": {k: v for k, v in updated_user.items()}
#     }
# if updated_user:
#     return ResponseModel(
#         "User with ID: {} name update is successful".format(id),
#         "User updated successfully",
#     )
# return ErrorResponseModel(
#     "An error occurred",
#     404,
#     "There was an error updating the user data.",
# )

# @router.put("/api/users/{user_id}", response_model=UserOut)


@router.delete("/api/users/{user_id}", response_model=bool)
def delete_user(user_id: str, queries: UserQueries = Depends()):
    queries.delete_user(user_id)
    return True
