from queries.users import UserQueries
from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


class fakeaccountout:
    def get_user(self, username):
        result = {"id": "1", "full_name": "full_name", "username": "username"}
        return result


def test_get_account():
    expected = {"id": 1, "full_name": "full_name", "username": "username"}
    app.dependency_overrides[UserQueries] = fakeaccountout
    response = client.get(
        "/api/users/1?username=username",
    )
    assert response.status_code == 200
    assert response.json() == expected
    app.dependency_overrides = {}
