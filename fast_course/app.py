from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user import User
from schemas.schema_user import (
    UserList,
    UserPublicSchema,
    UserSchema,
)
from settings.database import get_session

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Hello World'}


@app.post(
    '/users/', response_model=UserPublicSchema, status_code=HTTPStatus.CREATED
)
def create_user(user: UserSchema, session=Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if user.username == db_user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )

        elif user.email == db_user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    db_user = User(
        username=user.username, password=user.password, email=user.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList)
def read_users(limit: int = 10, session: Session = Depends(get_session)):
    user = session.scalars(select(User))

    return {'users': user}


@app.put('/users/{user_id}', response_model=UserPublicSchema, status_code=HTTPStatus.OK)
def update_user(user_id: int, user: User, session: Session = Depends(get_session)):
    user = session.scalar(select(user).where(User.id == user_id))

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'User id {user_id} not found'
        )


@app.delete('/users/{user_id}', response_model=UserPublicSchema, status_code=HTTPStatus.OK)
def delete_user(user_id: int, user: User, session: Session = Depends(get_session())):
    user = session.scalar(select(user).where(User.id == user_id))

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'User id {user_id} not found'
        )


