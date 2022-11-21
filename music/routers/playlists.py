from fastapi import APIRouter, Depends, Response
from queries.playlists import PlaylistQueries
from pydantic import BaseModel

from db import SongQueries

router = APIRouter()


class Song(BaseModel):
    id: str
    name: str
    artist: str
    uri: str


# class Playlist(BaseModel):
#     id: int
#     name: str
#     songs: list[Song]


class PlaylistIn(BaseModel):
    name: str
    songs: list[Song]


class PlaylistOut(BaseModel):
    id: int | str
    name: str
    songs: list[Song]


class PlaylistsOut(BaseModel):
    playlists: list[PlaylistOut]


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
@router.get("/api/playlists/", response_model=PlaylistsOut)
def get_all_playlists(queries: PlaylistQueries = Depends()):
    playlists = []
    for playlist in queries.get_all_playlists():
        playlist["id"] = str(playlist["_id"])
        playlists.append(playlist)
    return {"playlists": playlists}
    # return {
    #   "playlists": queries.get_all_playlists()
    # }


# get playlist by ID
@router.get("/api/playlists/{playlist_id}", response_model=PlaylistOut)
def get_playlist(
    playlist_id: str,
    response: Response,
    queries: PlaylistQueries = Depends(),
):
    record = queries.get_playlist(playlist_id)
    if record is None:
        response.status_code = 404
    else:
        return record


@router.post("/api/playlists/", response_model=PlaylistOut)
def create_playlist(
    playlist_in: PlaylistIn, queries: PlaylistQueries = Depends()
):
    return queries.create_playlist(playlist_in)


@router.get("/api/recommendations/")
def get_recommendations():
    # import requests
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
