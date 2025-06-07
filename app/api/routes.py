# app/api/routes.py
from fastapi import APIRouter
from app.schemas.input_schema import InputData
from app.services.predictor import predict_user

router = APIRouter()

@router.post("/predict")
def predict(input: InputData):
    return predict_user(input)
