from fastapi import FastAPI, Depends

# from queries.playlists import PlaylistsOut
# from db import PlaylistQueries as PlaylistQ
from routers import playlists
from routers import songs

app = FastAPI()

app.include_router(playlists.router)
app.include_router(songs.router)
# playlist bound for spotify
# @app.post("/api/playlist")
# def playlist():
#     return "X"


# playlist stored in database
# @app.post("/api/local_playlist")
# def local_playlist():
#     return "X"
