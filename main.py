from typing import Union
from fastapi import FastAPI

import api.models
import api.user_router
from database import engine
api.models.Base.metadata.create_all(bind=engine) #자동으로 테이블 생성 설정 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/test")
def read_test():
    return {"test":"done"}

app.include_router(router=api.user_router.user)