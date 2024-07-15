from http import HTTPStatus


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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'vitoria',
                'email': 'vitoria@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'password': '1235',
            'username': 'maria juliana',
            'email': 'teste@teste.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'maria juliana',
        'email': 'teste@teste.com',
        'id': 1,
    }
