from fastapi import FastAPI, Depends
from models import Playlist
from db import PlaylistQueries as PlaylistQ

app = FastAPI()

@app.get("/api/playlists", response_model=Playlist)
def list_playlists(queries: PlaylistQ = Depends()):
    return{
        "playlists": queries.get_all_playlists(),
    }

