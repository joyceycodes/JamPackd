from fastapi import APIRouter, Depends, Response
from pydantic import BaseModel
from queries.users import UserQueries

router = APIRouter()


class UserIn(BaseModel):
    first: str
    last: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int | str
    first: str
    last: str
    email: str
    password: str


class UsersOut(BaseModel):
    users: list[UserOut]


@router.post("/api/users", response_model=UserIn)
def create_user(user_in: UserIn, queries: UserQueries = Depends()):
    return queries.create_user(user_in)


# @router.get("/api/users", response_model=UsersOut)
# def users_list(queries: UserQueries = Depends()):
#     return {
#         "users": queries.get_all_users(),
#     }


@router.get("/api/users/{user_id}", response_model=UserOut)
def get_single_user(
    user_id: str,
    response: Response,
    queries: UserQueries = Depends(),
):
    record = queries.get_user(user_id)
    print(record)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.delete("/api/users/{user_id}", response_model=bool)
def delete_user(user_id: str, queries: UserQueries = Depends()):
    queries.delete_user(user_id)
    return True
