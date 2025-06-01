from fastapi import FastAPI
from typing import List, Union
from app.database import Base, engine
from datetime import datetime, time, timedelta
from app.users.router import user_router 
from app.security.router import security_router
from app import all_models
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(security_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}