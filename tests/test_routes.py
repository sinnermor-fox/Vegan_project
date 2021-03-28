import flask
import pytest
from app import app as flask_app


@pytest.fixture(autouse=True)
def app():
    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_menu_username(client):
    response = client.get('/menu/sinnermor')
    assert response.status_code == 200