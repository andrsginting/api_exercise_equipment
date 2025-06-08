# app/main.py
from fastapi import FastAPI
from app.api.routes import router

# Trigger download of multi_model.pkl if not present
import app.utils.download_model  # <- asumsikan file ini sudah berada di app/utils

app = FastAPI(
    title="GymBro Fitness API",
    description="API untuk rekomendasi fitness goal, exercises, dan equipment.",
    version="1.0.0"
)

app.include_router(router)
