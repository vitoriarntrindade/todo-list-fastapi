from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_jwt_invalid_token(
    client,
):
    response = client.delete(
        '/users/2', headers={'Authorization': 'Bearer invalid token'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_valid_user_exists(client, token):
    response = client.delete(
        '/users/12', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.json() == {'detail': 'Not enought permissions'}
