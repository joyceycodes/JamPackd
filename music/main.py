from fastapi import FastAPI, Depends
from routers import playlists
from routers import spotify

app = FastAPI()

app.include_router(playlists.router)
app.include_router(spotify.router)
