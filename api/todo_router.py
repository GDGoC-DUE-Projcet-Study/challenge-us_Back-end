from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter,Depends,HTTPException

from api import todo_crud
from api import todo_schema

todo = APIRouter(
        prefix="/todo",
        tags=["todo"]
)

@todo.post(path="/create", description="목표 생성")
async def create_todo(id,new_todo:todo_schema.CreateTodo,db: Session = Depends(get_db)):
    res = todo_crud.post_todo(id,new_todo, db)
    if res=="목표 등록 실패":
        raise HTTPException(status_code=400)
    return res

@todo.get(path="/get/{owner_id}", description="회원별 전체 목표 조회")
async def get_todo_list(owner_id,db:Session=Depends(get_db)):
    res=todo_crud.get_todo_list(owner_id,db)
    if res==None:
        raise HTTPException(status_code=404)
    return res

@todo.get(path="/get/{todo_idx}", description="개별 목표 조회")
async def get_todo(todo_idx:str,db:Session=Depends(get_db)):
    res = todo_crud.get_todo(todo_idx,db)
    if res==None:
        raise HTTPException(status_code=404)
    return "개별 목표 조회"

@todo.put(path="/update", description="목표 수정")
async def update_todo(id,idx:str,update_todo:todo_schema.UpdateTodo,db:Session=Depends(get_db)):
    res = todo_crud.update_todo(id,idx,update_todo,db)
    return res

@todo.delete(path="/delete", description="목표 삭제")
async def delete_todo(id,idx,db:Session=Depends(get_db)):
    res=todo_crud.delete_user(id,idx,db)
    
    if res==None:
        raise HTTPException(status_code=404)
    return res



