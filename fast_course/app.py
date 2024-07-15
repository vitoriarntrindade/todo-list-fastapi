from http import HTTPStatus

from fastapi import FastAPI

from schemas.schema_user import DbMockSchema, UserPublicSchema, UserSchema

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
