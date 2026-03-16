from fastapi import FastAPI
from src.routers import metrics, users

app = FastAPI()

app.include_router(metrics.router)
app.include_router(users.router)
