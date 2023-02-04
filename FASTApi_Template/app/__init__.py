from fastapi import FastAPI
from controllers import home

def create_app():
    ## Create APP Object
    app = FastAPI()

    ## Registering your routes and routers
    app.include_router(home)
    
    return app