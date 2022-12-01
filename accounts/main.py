import os
from routers import users

# from queries.users import UserIn
from pydantic import BaseModel
from fastapi import FastAPI, Request
from authenticator import authenticator
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8001",
    "http://localhost:8003",
    "http://localhost:8081",
    os.environ.get("CORS_HOST", None),
]
# may need to change this url above MAYBE


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(authenticator.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root(request: Request):
    print(request)
    return {}


# import UserIn
@app.put("/users/{id}")
async def remove_hashing_password(UserIn):
    data = UserIn
    data.pop("hashed_password")
