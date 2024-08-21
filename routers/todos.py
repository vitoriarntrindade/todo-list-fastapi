from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

# from models.todo import Todo
from models.user import Todo, User
from schemas.todo_schema import TodoList, TodoPublic, TodoSchema
from security import get_current_user
from settings.database import get_session

Session = Annotated[Session, Depends(get_session)]
User = Annotated[User, Depends(get_current_user)]

router = APIRouter(prefix='/todos', tags=['todos'])


@router.post('/', response_model=TodoPublic)
def create_todo(todo: TodoSchema, session: Session, user: User):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo


@router.get('/', response_model=TodoList)
def list_todos(
    session: Session,
    user: User,
    title: str | None = None,
    description: str | None = None,
    state: str | None = None,
    offset: str | None = None,
    limit: str | None = None,
):
    query = select(Todo).where(Todo.user_id == user.id)

    if title:
        query = query.filter(Todo.title.contains(title))

    if description:
        query = query.filter(Todo.description.contains(description))

    if state:
        query = query.filter(Todo.state.contains(state))

    todos = session.scalars(query.offset(offset).limit(limit)).all()

    return {'todos': todos}
