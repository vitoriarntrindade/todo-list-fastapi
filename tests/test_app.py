from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_course.app import app

client = TestClient(app)


def test_root_should_returns_ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}
