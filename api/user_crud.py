from sqlalchemy.orm import Session

from api.models import User
from api.user_schema import CreateUser
def insert_user(new_user:CreateUser,db:Session):
    user = User(
        id = new_user.id,
        pw = new_user.pw,
        name = new_user.name
    )
    db.add(user)
    db.commit()

    return "회원가입완료"