from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routers import playlists
from routers import spotify
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get(
            "CORS_HOST",
            # "http://localhost:3000",
            "http://localhost:8003",
        )
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(playlists.router)
# app.include_router(spotify.router)
