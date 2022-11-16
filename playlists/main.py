from fastapi import FastAPI, Depends
from queries.playlists import PlaylistsOut
from db import PlaylistQueries as PlaylistQ
from routers import playlists

app = FastAPI()

app.include_router(playlists.router)

