from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter,Depends,HTTPException

from api import user_schema
from api import user_crud

user = APIRouter(
        prefix="/user",
        tags=["user"]
)

@user.post(path="/create", description="회원가입 - 유저 생성")
async def create_user(new_user:user_schema.CreateUser,db: Session = Depends(get_db)): 
    res = user_crud.insert_user(new_user, db)
    if res !="회원가입완료":
        raise HTTPException(status_code=422)
    return res

@user.get(path="/get", description="전체 회원 조회")
async def get_all_user(db:Session=Depends(get_db)):
    res=user_crud.get_all_user(db)
    if res!=None:
        raise HTTPException(status_code=422)
    return res

@user.get(path="/get/{user_id}", description="개인 회원 조회")
async def get_user(user_id:str,db:Session=Depends(get_db)):
    res = user_crud.get_user(user_id,db)
    if res==None:
        raise HTTPException(status_code=404)
    return res

@user.put(path="/update/{user_id}", description="회원 정보 수정")
async def update_user(user_id:str,update_user:user_schema.UpdateUser,db:Session=Depends(get_db)):
    res = user_crud.update_user(user_id,update_user,db)
    if res !="수정완료":
        raise HTTPException(status_code=409)
    return res


@user.delete(path="/delete",description="회원삭제")
async def delete_user(delete_user:user_schema.DeleteUser,db:Session=Depends(get_db)):
    res =user_crud.delete_user(delete_user,db)
    if res !="회원 삭제":
        raise HTTPException(status_code=404)
    return res

