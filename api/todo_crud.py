from sqlalchemy.orm import Session

from api.models import Todo,User
from api.todo_schema import CreateTodo,UpdateTodo


def post_todo(id,new_todo:CreateTodo,db:Session):
    # if db.query(User).filter(User.id==id).first()==None:
    #     return "목표 등록 실패"
    todo=Todo(
        owner_id = id,
        title = new_todo.title,
        description = new_todo.description
    )
    db.add(todo)
    db.commit()

    todo_list=db.query(Todo).filter(Todo.owner_id==id).all()

    return todo_list

def get_todo_list(owner_id,db:Session):
    todo_list=db.query(Todo).filter(Todo.owner_id==owner_id).all()
    print(todo_list)
    return todo_list

def get_todo(idx,db:Session):
    todo = db.query(Todo).filter(Todo.idx==idx).first()
    return todo

def update_todo(idx,update_todo:UpdateTodo,db:Session):
    todo = db.query(Todo).filter(Todo.idx==idx).first()
    
    todo.title = update_todo.title
    todo.description = update_todo.description
    todo.percent = update_todo.percent
    if todo.percent>99.9:
        todo.complete=True

    db.add(todo)
    db.commit()

    return "수정완료"

def delete_user(idx,db:Session):
    todo=db.query(Todo).filter(Todo.idx==idx).delete()
    if todo==None:
        return None
    db.commit()

    return "목표 삭제"


