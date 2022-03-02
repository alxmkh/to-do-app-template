from fastapi import FastAPI
from api import api
from routers import routers

app = FastAPI(title='TODO API', prefix="/api",)
app.include_router(api.router)
app.include_router(routers.router)
