from sqlalchemy import select

from models.user import User


def test_create_user(session):
    new_user = User(username='raymara', password='123', email='ray@teste.com')

    session.add(new_user)
    session.commit()

    result = session.scalar(select(User).filter_by(email='ray@teste.com'))

    assert result.username == 'raymara'
    assert result.id == 1
