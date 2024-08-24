from pydantic import BaseModel

from models.todo_state import TodoState


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState


class TodoPublic(TodoSchema):
    id: int


class TodoList(BaseModel):
    todos: list[TodoPublic]


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: TodoState | None = None


class Message(BaseModel):
    message: str
