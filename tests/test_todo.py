from http import HTTPStatus

from models.todo_state import TodoState
from tests.conftest import TodoFactory


def test_create_todo(client, token):
    response = client.post(
        '/todos/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'title': 'Test ToDo',
            'description': 'Test description',
            'state': 'draft',
        },
    )
    assert response.json() == {
        'id': 1,
        'title': 'Test ToDo',
        'description': 'Test description',
        'state': 'draft',
    }


def test_list_todos_should_return_5_todos(session, token, user, client):
    expected_todos = 5

    session.bulk_save_objects(TodoFactory.create_batch(5, user_id=user.id))
    session.commit()

    response = client.get(
        '/todos/', headers={'Authorization': f'Bearer {token}'}
    )

    assert len(response.json()['todos']) == expected_todos


def test_list_todos_pagination_should_return_3(session, token, user, client):
    expected_todos = 2

    session.bulk_save_objects(TodoFactory.create_batch(5, user_id=user.id))
    session.commit()

    response = client.get(
        '/todos/?offset=1&limit=2',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['todos']) == expected_todos


def test_list_todos_filter_title_should_return_4(session, token, user, client):
    expected_todos = 4

    session.bulk_save_objects(
        TodoFactory.create_batch(4, user_id=user.id, title='Test todo 1')
    )
    session.commit()

    response = client.get(
        '/todos/?title=Test todo 1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['todos']) == expected_todos


def test_list_todos_filter_description_should_return_6(
    session, token, user, client
):
    expected_todos = 6

    session.bulk_save_objects(
        TodoFactory.create_batch(6, user_id=user.id, description='Test todo 1')
    )
    session.commit()

    response = client.get(
        '/todos/?description=Test todo 1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['todos']) == expected_todos


def test_list_todos_filter_state_should_return_6(session, token, user, client):
    expected_todos = 6

    session.bulk_save_objects(
        TodoFactory.create_batch(6, user_id=user.id, state=TodoState.done)
    )
    session.commit()

    response = client.get(
        '/todos/?state=done',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['todos']) == expected_todos


def test_list_todos_filter_combined_should_return_5_todos(
    session, user, client, token
):
    expected_todos = 5
    session.bulk_save_objects(
        TodoFactory.create_batch(
            5,
            user_id=user.id,
            title='Test todo combined',
            description='combined description',
            state=TodoState.done,
        )
    )

    session.bulk_save_objects(
        TodoFactory.create_batch(
            3,
            user_id=user.id,
            title='Other title',
            description='other description',
            state=TodoState.todo,
        )
    )
    session.commit()

    response = client.get(
        '/todos/?title=Test todo combined&description=combined&state=done',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['todos']) == expected_todos


def test_delete_todo(session, client, token, user):
    todo = TodoFactory(user_id=user.id)
    session.add(todo)
    session.commit()

    response = client.delete(
        f'todos/{todo.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Task has been deleted successfully'}


def test_delete_return_error(client, token):
    response = client.delete(
        f'/todos/{10}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_patch_todo(client, token, session, user):
    todo = TodoFactory(user_id=user.id)

    session.add(todo)
    session.commit()

    response = client.patch(
        f'/todos/{todo.id}',
        json={'title': 'teste!'},
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
