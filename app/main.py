from fastapi import FastAPI

from app.api.api import router

app = FastAPI(title="Knowledge Hub")
app.include_router(router)
