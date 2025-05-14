from fastapi import FastAPI
from typing import List, Union
from app.database import Base, engine
from datetime import datetime, time, timedelta
from app.users.router import user_router 

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}