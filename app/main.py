# app/main.py
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="GymBro Fitness API",
    description="API untuk rekomendasi fitness goal, exercises, dan equipment.",
    version="1.0.0"
)

app.include_router(router)
