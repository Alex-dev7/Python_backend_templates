from fastapi import APIRouter

##########################################
## Setup Your Routes in This File
##########################################

home = APIRouter(prefix="")

@home.get("/")
async def home_home():
    return {"home": "The Homepage"}