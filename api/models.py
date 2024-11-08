from sqlalchemy import Column,Integer,VARCHAR,DateTime,ForeignKey,String,Boolean
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__="User"

    id = Column(VARCHAR(30),primary_key=True,nullable=False)
    pw = Column(VARCHAR(30), nullable=False)
    name = Column(String,nullable=False)
    createdate = Column(DateTime,nullable=False,default=datetime.now)
    phone = Column(String,nullable = False)

    todo = relationship("Todo",back_populates="owner")

class Todo(Base):
    __tablename__="Todo"

    idx = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)
    complete = Column(Boolean,default=False) #달성도 %

    owner_id = Column(VARCHAR(30),ForeignKey("User.id"))

    owner= relationship("User",back_populates="todo")
