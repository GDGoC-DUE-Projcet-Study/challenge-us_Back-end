from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter,Depends

from api import user_schema
from api import user_crud

user = APIRouter(
        prefix="/user",
)

@user.post(path="/create", description="회원가입 - 유저 생성")
async def create_user(new_user:user_schema.CreateUser,db: Session = Depends(get_db)):
    return user_crud.insert_user(new_user, db)

@user.get(path="/get", description="전체 회원 조회")
async def get_all_user(db:Session=Depends(get_db)):
    return user_crud.get_all_user(db)

@user.get(path="/get/{user_id}", description="개인 회원 조회")
async def get_user(user_id:str,db:Session=Depends(get_db)):
    return user_crud.get_user(user_id,db)

@user.put(path="/update/{user_id}", description="회원 정보 수정")
async def update_user(user_id:str,db:Session=Depends(get_db)):
    return user_crud.update_user(user_id,db)
