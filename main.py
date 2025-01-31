from fastapi import FastAPI
from api.routers.router import router

app = FastAPI(docs_url='/fibonacci/docs')

app.include_router(router, prefix='/fibonacci')