from fastapi import FastAPI, Request
from routers import users
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


app = FastAPI()


app.include_router(users.router)


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8001",
    "http://localhost:8003",
    "http://localhost:8081",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# async def main():
#     return {"message": "Hello World"}


class UserIn(BaseModel):
    hashed_password: str
    id: int | str
    full_name: str
    email: str


@app.get("/")
async def read_root(request: Request):
    print(request)
    return {}


@app.put("/users/{id}")
async def remove_hashing_password(UserIn):
    data = UserIn
    data.pop("hashed_password")
