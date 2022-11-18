from fastapi import FastAPI, Depends

# from queries.playlists import PlaylistsOut
# from db import PlaylistQueries as PlaylistQ
from routers import playlists

app = FastAPI()

app.include_router(playlists.router)

# playlist bound for spotify
@app.post("/api/playlist")
def playlist():
    return "X"


# playlist stored in database
# @app.post("/api/local_playlist")
# def local_playlist():
#     return "X"
