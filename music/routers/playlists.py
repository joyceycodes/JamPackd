from fastapi import APIRouter, Depends, Response
from queries.playlists import PlaylistQueries
from pydantic import BaseModel

from db import SongQueries

router = APIRouter()


class Playlist(BaseModel):
    _id: int
    name: str
    songs: list


class PlaylistIn(BaseModel):
    _id: int
    name: str
    songs: list


class PlaylistOut(BaseModel):
    _id: int
    name: str
    songs: list


class PlaylistsOut(BaseModel):
    playlists: list[Playlist]


class Song(BaseModel):
    title: str
    artist: str
    durratioin: str
    # album_art: img --not sure what the correct tag is for images
    uri: str


class SongOut(BaseModel):
    id: int | str
    title: str
    artist: str
    durratioin: str
    uri: str


class SongsOut(BaseModel):
    songs: list[SongOut]


# get all playlists
@router.get("/api/playlists", response_model=PlaylistsOut)
def list_playlists(queries: PlaylistQueries = Depends()):
    return {
        "playlists": queries.get_all_playlists(),
    }


# get playlist by ID
@router.get("/api/playlists/{id}", response_model=Playlist)
def get_playlist_detail():
    return Playlist


@router.get("/api/recommendations")
def get_recommendations():
    pass


# get all songs
@router.get("/api/songs", response_model=SongsOut)
def songs_list(queries: SongQueries = Depends()):
    return {
        "songs": queries.get_all_songs(),
    }


# get individual song
@router.get("/api/songs/{song_id}", response_model=SongOut)
def get_song(
    id: str,
    response: Response,
    queries: SongQueries = Depends(),
):
    record = queries.get_song(id)
    print(record)
    if record is None:
        response.status_code = 404
    else:
        return record


# create a song
@router.post("api/songs/", response_model=SongOut)
def create_song(song_in: Song, queries: SongQueries = Depends()):
    return queries.create_song(song_in)


# update song to list(?)
@router.put("/api/songs/{song_id}", response_model=SongOut)
def update_song(
    song_id: str,
    song_in: Song,
    response: Response,
    queries: SongQueries = Depends(),
):
    record = queries.update_song(song_id, song_in)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.delete("/api/songs/{song_id}", response_model=bool)
def delete_song(song_id: str, queries: SongQueries = Depends()):
    queries.delete_user(song_id)
    return True
