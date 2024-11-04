from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter,Depends

from api import todo_crud
from api import todo_schema

todo = APIRouter(
        prefix="/todo",
        tags=["todo"]
)

@todo.post(path="/create", description="목표 생성")
async def create_todo(new_todo:todo_schema.CreateTodo,db: Session = Depends(get_db)):
    return todo_crud.post_todo(new_todo, db)

@todo.get(path="/get", description="전체 목표 조회")
async def get_todo_list(db:Session=Depends(get_db)):
    return todo_crud.get_todo_list(db)

@todo.get(path="/get/{todo_idx}", description="개별 목표 조회")
async def get_todo(todo_idx:str,db:Session=Depends(get_db)):
    return todo_crud.get_todo(todo_idx,db)

@todo.put(path="/update/{todo_idx}", description="목표 수정")
async def update_todo(todo_idx:str,update_todo:todo_schema.UpdateTodo,db:Session=Depends(get_db)):
    return todo_crud.update_todo(todo_idx,update_todo,db)


