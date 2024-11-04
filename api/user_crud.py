from sqlalchemy.orm import Session

from api.models import User
from api.user_schema import CreateUser,UpdateUser

def insert_user(new_user:CreateUser,db:Session):
    user = User(
        id = new_user.id,
        pw = new_user.pw,
        name = new_user.name
    )
    db.add(user)
    db.commit()

    return "회원가입완료"

def get_all_user(db:Session):
    user_list = db.query(User).all()
    return user_list

def get_user(id,db:Session):
    user = db.query(User).filter(User.id==id).first()
    return user

def update_user(id,update_user:UpdateUser,db:Session):
    user = db.query(User).filter(User.id==id).first()

    user.pw = update_user.pw
    user.name = update_user.name

    db.add(user)
    db.commit()

    return 수정완료