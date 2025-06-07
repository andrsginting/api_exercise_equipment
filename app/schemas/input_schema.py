# app/schemas/input_schema.py
from pydantic import BaseModel

class InputData(BaseModel):
    Sex: str
    Age: int
    Height: float
    Weight: float
    Hypertension: str
    Diabetes: str
