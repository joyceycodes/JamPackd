from fastapi import APIRouter, Depends, Response, Body
from pydantic import BaseModel, EmailStr
from db import UserQueries

router = APIRouter()


class UserIn(BaseModel):
    first: str
    last: str
    email: str
    username: str


class UserOut(BaseModel):
    id: int | str
    first: str
    last: str
    email: str
    username: str


class UsersOut(BaseModel):
    users: list[UserOut]


class UpdateUser(BaseModel):
    first: str
    last: str
    email: EmailStr
    username: str

    class Config:
        schema_extra = {
            "example": {
                "first": "z",
                "last": "z",
                "email": "z@z.com",
                "username": "Z",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}


@router.get("/api/users", response_model=UsersOut)
def users_list(queries: UserQueries = Depends()):
    return {
        "users": queries.get_all_users(),
    }


@router.get("/api/users/{user_id}", response_model=UserOut)
def get_user(
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


@router.post("/api/users/", response_model=UserOut)
def create_user(user_in: UserIn, queries: UserQueries = Depends()):
    return queries.create_user(user_in)


@router.put("/api/users/{user_id}", response_model=UserOut)
def update_user(id: str, req: UpdateUser = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = update_user(id, req)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )


#     user_id: str,
#     user_in: UserIn,
#     response: Response,
#     queries: UserQueries = Depends(),
# ):
#     record = queries.update_user(user_id, user_in)
#     if record is None:
#         response.status_code = 404
#     else:
#         return record


@router.delete("/api/users/{user_id}", response_model=bool)
def delete_user(user_id: str, queries: UserQueries = Depends()):
    queries.delete_user(user_id)
    return True
