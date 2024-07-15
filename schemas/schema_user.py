from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr


class DbMockSchema(UserSchema):
    id: int
