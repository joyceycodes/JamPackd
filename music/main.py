from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import playlists, spotify
import os

app = FastAPI()

origins = [
    os.environ.get("CORS_HOST", "REACT_APP_API_HOST"),
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


app.include_router(playlists.router)
app.include_router(spotify.router)
