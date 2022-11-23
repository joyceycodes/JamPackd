from fastapi import FastAPI, Depends
from routers import playlists
<<<<<<< HEAD
from routers import spotify
=======
from routers import songs
>>>>>>> main

app = FastAPI()

app.include_router(playlists.router)
<<<<<<< HEAD
app.include_router(spotify.router)
=======
app.include_router(songs.router)
# playlist bound for spotify
# @app.post("/api/playlist")
# def playlist():
#     return "X"


# playlist stored in database
# @app.post("/api/local_playlist")
# def local_playlist():
#     return "X"
>>>>>>> main
