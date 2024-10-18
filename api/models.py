from sqlalchemy import Column,Integer,VARCHAR,DateTime
from datetime import datetime

from database import Base

class User(Base):
    __tablename__="User"

    id = Column(VARCHAR(30),primary_key=True,nullable=False)
    pw = Column(VARCHAR(30), nullable=False)
    name = Column(VARCHAR(50),nullable=False)
    createdate = Column(DateTime,nullable=False,default=datetime.now)