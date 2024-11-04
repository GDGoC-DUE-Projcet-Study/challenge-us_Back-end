from sqlalchemy.orm import Session

from api.models import Todo
from api.todo_schema import CreateTodo,UpdateTodo

def post_todo(new_todo:CreateTodo,db:Session):
    todo=Todo(
        title = new_todo.title,
        description = new_todo.description
    )
    db.add(todo)
    db.commit()

    return "목표 등록 완료"

def get_todo_list(db:Session):
    todo_list=db.query(Todo).all()
    return todo_list

def get_todo(idx,db:Session):
    todo = db.query(Todo).filter(Todo.idx==idx).first()
    return todo

def update_todo(idx,update_todo:UpdateTodo,db:Session):
    todo = db.query(Todo).filter(Todo.idx==idx).first()

    todo.title = update_todo.title
    todo.description = update_todo.description

    db.add(todo)
    db.commit()

    return "수정완료"



