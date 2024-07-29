from datetime import datetime, timedelta
from http import HTTPStatus

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, encode
from jwt.exceptions import PyJWTError
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session
from zoneinfo import ZoneInfo

from models.user import User
from settings.database import get_session

pwd_context = PasswordHash.recommended()
oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = 'testsecretkey'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRES_MINUTES = 30


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_passowrd: str):
    return pwd_context.verify(plain_password, hashed_passowrd)


def create_access_token(data_payload: dict):
    to_encode = data_payload.copy()

    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRES_MINUTES
    )

    to_encode.update({'exp': expire})

    enconded_jwt = encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return enconded_jwt


def get_current_user(
    session: Session = Depends(get_session),
    token=Depends(oauth2_schema),
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = decode(token, SECRET_KEY, ALGORITHM)
        username: str = payload.get('sub')

        if not username:
            raise credentials_exception

    except PyJWTError:
        raise credentials_exception

    user_db = session.scalar(select(User).where(User.email == username))

    if user_db is None:
        raise credentials_exception

    return user_db
