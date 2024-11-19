from sqlalchemy.orm import Session

from api.models import User
from api.user_schema import CreateUser,UpdateUser,DeleteUser

from passlib.context import CryptContext
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain,hash):
    return bcrypt_context.verify(plain,hash)

def insert_user(new_user:CreateUser,db:Session):
    hashpass=get_password_hash(new_user.pw)
    user = User(
        id = new_user.id,
        pw = hashpass,
        name = new_user.name,
        phone = new_user.phone
    )
    db.add(user)
    db.commit()

    return "회원가입완료"

#admin 비번 확인
def get_all_user(id,pw,db:Session):
    admin= db.query(User).filter(User.id==id).first()
    if verify_password(pw,admin.pw):
        user_list=db.query(User).all()
        return user_list
    return "관리자가 아닙니다"

def get_user(id,db:Session):
    user = db.query(User).filter(User.id==id).first()
    return user

def update_user(id,update_user:UpdateUser,db:Session):
    user = db.query(User).filter(User.id==id).first()

    user.pw = update_user.pw
    user.name = update_user.name

    db.add(user)
    db.commit()

    return "수정완료"

def delete_user(delete_user:DeleteUser,db:Session):
    user = db.query(User).filter(User.id==delete_user.id).first()
    if user.pw==delete_user.pw:
        db.query(User).filter(User.id==delete_user.id).delete()
    
    db.commit()

    return "회원 삭제"