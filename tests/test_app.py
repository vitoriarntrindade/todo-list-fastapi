from http import HTTPStatus

from schemas.schema_user import UserPublicSchema


def test_root_should_returns_ok(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'vitoria',
            'email': 'vitoria@example.com',
            'password': 'senha123',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'vitoria',
        'email': 'vitoria@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublicSchema.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.json() == {'users': [user_schema]}


def test_update_users(client, user):
    response = client.put(
        '/users/1',
        json={
            'password': '1235',
            'username': 'maria juliana',
            'email': 'teste@teste.com',
        },
    )

    assert response.json() == {
        'username': 'maria juliana',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_create_user_username_duplicated_returns_400(client, user):
    response = client.post(
        '/users',
        json={
            'username': 'Teste',
            'email': 'teste@teste.com',
            'password': 'senha123',
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Username already exists'}
