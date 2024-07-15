from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_course.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_should_returns_ok(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'vitoria',
            'email': 'vitoria@gmail.com',
            'password': '132@@JHKJ',
        },
    )

    # Validando se o status_code está correto
    assert response.status_code == HTTPStatus.CREATED
    # Validando UserPublicSchema
    assert response.json() == {
        'username': 'vitoria',
        'email': 'vitoria@gmail.com',
        'id': 1,
    }
