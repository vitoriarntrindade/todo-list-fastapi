from http import HTTPStatus

from schemas.schema_user import UserPublicSchema


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


def test_update_users(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
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


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )

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


def test_update_wrong_users_forbidden(client, user, token):
    response = client.put(
        f'/users/{user.id + 2}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'password': '1235',
            'username': 'maria juliana',
            'email': 'teste@teste.com',
        },
    )

    assert response.json() == {'detail': 'Not enought permissions'}


def test_delete_wrong_user(client, user, token):
    response = client.delete(
        f'/users/{user.id + 1}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.json() == {'detail': 'Not enought permissions'}
