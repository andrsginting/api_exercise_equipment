# app/schemas/input_schema.py
from pydantic import BaseModel, Field

class InputData(BaseModel):
    Sex: int = Field(..., ge=0, le=1, description="1 untuk Pria, 0 untuk Wanita")
    Age: int = Field(..., gt=0, description="Usia harus lebih dari 0")
    Height: float = Field(..., gt=0, description="Tinggi badan dalam meter (contoh: 1.75)")
    Weight: float = Field(..., gt=0, description="Berat badan dalam kg (contoh: 68.5)")
    Hypertension: int = Field(..., ge=0, le=1, description="1 jika memiliki hipertensi, 0 jika tidak")
    Diabetes: int = Field(..., ge=0, le=1, description="1 jika memiliki diabetes, 0 jika tidak")

    class Config:
        json_schema_extra = {
            "example": {
                "Sex": 1,
                "Age": 28,
                "Height": 1.75,
                "Weight": 72,
                "Hypertension": 0,
                "Diabetes": 0
            }
        }