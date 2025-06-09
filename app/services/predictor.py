# app/services/predictor.py
import joblib
import numpy as np
import json
import os
from app.utils.preprocessing import preprocess_input
from download_model import download_model

# Pastikan model multi-label sudah tersedia
download_model()

# Load model dan data
goal_model = joblib.load("app/models/goal_model.pkl")
multi_model = joblib.load("app/models/multi_model.pkl")
scaler = joblib.load("app/models/scaler.pkl")
mlb_ex = joblib.load("app/models/mlb_ex.pkl")
mlb_eq = joblib.load("app/models/mlb_eq.pkl")

with open("app/assets/goal_mapping.json", "r") as f:
    goal_mapping = json.load(f)

def predict_user(input):
    input_data = preprocess_input(input.dict(), scaler)
    input_data = np.array(input_data).reshape(1, -1)

    # Goal prediction
    goal_pred = goal_model.predict(input_data)[0]
    goal_result = goal_mapping[str(goal_pred)]

    # Multi-label prediction
    multi_pred = multi_model.predict(input_data)[0]
    ex_len = len(mlb_ex.classes_)
    eq_len = len(mlb_eq.classes_)

    exercise_result = [mlb_ex.classes_[i] for i in range(ex_len) if multi_pred[i]]
    equipment_result = [mlb_eq.classes_[i - ex_len] for i in range(ex_len, ex_len + eq_len) if multi_pred[i]]

    return {
        "Fitness Goal": goal_result,
        "Recommended Exercises": exercise_result,
        "Required Equipment": equipment_result
    }
