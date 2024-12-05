from typing import Union
import api.todo_router
from fastapi import FastAPI

import api.models
import api.user_router
from database import engine
api.models.Base.metadata.create_all(bind=engine) #자동으로 테이블 생성 설정 

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",
]

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(router=api.user_router.user)
app.include_router(router=api.todo_router.todo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)