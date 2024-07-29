from http import HTTPStatus

from fastapi import FastAPI

from routers.auth import router as auth
from routers.users import router as users

app = FastAPI()
app.include_router(users)
app.include_router(auth)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Hello World'}
