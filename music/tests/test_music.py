from fastapi.testclient import TestClient
from queries.playlists import PlaylistQueries
from authenticator_music import authenticate
from main import app

client = TestClient(app)


class EmptyPlaylistQueries:
    def get_all_playlists(self):
        return []

    def delete_playlist(self, id):

        return True


# def test_get_all_playlists():
#     app.dependency_overrides[PlaylistQueries] = EmptyPlaylistQueries
#     response = client.get("/api/playlists")
#     assert response.status_code == 200
#     assert response.json() == {"playlists": []}

#     app.dependency_overrides = {}


def test_delete_playlist():

    account = {"id": 123}
    app.dependency_overrides[PlaylistQueries] = EmptyPlaylistQueries
    app.dependency_overrides[
        authenticate.get_current_account_data
    ] = lambda: account

    response = client.delete("api/playlists/1")

    assert response.status_code == 200
    assert response.json() == True  # noqa

    app.dependency_overrides = {}


# class MockPlaylistQueries:
#     def create_playlist(self, data, user_id):
#         playlist_good = {
#         {
#             "id": 0,
#             "name": "Test Playlist",
#             "songs": [{"name": "string",
# "artist": "string", "uri": "string"}],
#             "comments": "Tasty comments here",
#         },
#         }
#         playlist_good.get_playlist(data, user_id)
#         return playlist_good


#     def test_create_playlist():
#         json = PlaylistIn(
#             id="",
#             name = "Test Playlist",
#             songs: [],
#             comments = "Tasty comments here"
#         )

#     expected = {

#     }


# playlist_good = {
#     {
#         "id": 0,
#         "name": "Test Playlist",
#         "songs": [{"name": "string", "artist": "string", "uri": "string"}],
#         "comments": "Tasty comments here",
#     }
# }


# def test_create_playlist():
#     app.dependency_overrides[PlaylistQueries] = MockPlaylistQueries
#     reponse = client.post("/api/playlists")
#     assert reponse.status_code == 200
#     assert reponse.json() == playlist_good
