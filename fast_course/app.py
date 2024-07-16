from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from schemas.schema_user import (
    DbMockSchema,
    UserList,
    UserPublicSchema,
    UserSchema,
)

app = FastAPI()

database_mock = []


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Hello World'}


@app.post(
    '/users/', response_model=UserPublicSchema, status_code=HTTPStatus.CREATED
)
def create_user(user: UserSchema):
    user_with_id = DbMockSchema(id=len(database_mock) + 1, **user.model_dump())

    database_mock.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UserList, status_code=HTTPStatus.OK)
def read_users():
    return {'users': database_mock}


@app.put(
    '/users/{user_id}',
    response_model=UserPublicSchema,
    status_code=HTTPStatus.OK,
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = DbMockSchema(**user.model_dump(), id=user_id)
    if not user_with_id:
        raise HTTPException(status_code=404, detail='User not found')
    database_mock[user_id - 1] = user_with_id

    return user_with_id
