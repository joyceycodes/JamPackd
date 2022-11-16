from fastapi import APIRouter, Depends
from queries.playlists import PlaylistQueries
from pydantic import BaseModel

router = APIRouter()

class Playlist(BaseModel):
    name: str
    user_id: int

class PlaylistsOut(BaseModel):
    playlists: list[Playlist]

# get all playlists
@router.get("/api/playlists", response_model=PlaylistsOut)
def list_playlists(queries: PlaylistQueries = Depends()):
    return{
        "playlists": queries.get_all_playlists(),
    }

# get playlist by ID
@router.get("/api/playlists/{id}", response_model=Playlist)
def get_playlist_detail(int: id):
    return Playlist
