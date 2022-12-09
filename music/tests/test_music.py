from fastapi.testclient import TestClient
from queries.playlists import PlaylistQueries
from main import app
from authenticator_music import authenticate

client = TestClient(app)


class EmptyPlaylistQueries:
    def get_all_playlists(sel, user_id):
        return []


def test_get_all_playlists():

    # Arrange
    account = {"id": 123}
    app.dependency_overrides[PlaylistQueries] = EmptyPlaylistQueries
    app.dependency_overrides[
        authenticate.get_current_account_data
    ] = lambda: account

    # Act
    response = client.get("/api/playlists")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"playlists": []}

    # Clean up
    app.dependency_overrides = {}
