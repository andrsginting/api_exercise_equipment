# app/services/predictor.py
import joblib
import numpy as np
import json
import os
from app.utils.preprocessing import prepare_feature_array # <-- Ganti nama fungsi yang diimpor
# from download_model import download_model # Baris ini bisa dihapus jika file sudah ada di repo

# Cek dan load semua model dan aset yang diperlukan
# Pastikan semua file ini ada di dalam direktori app/models/ dan app/assets/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

goal_model = joblib.load(os.path.join(MODEL_DIR, "goal_model.pkl"))
multi_model = joblib.load(os.path.join(MODEL_DIR, "multi_model.pkl")) # File ini didownload atau sudah ada
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
mlb_ex = joblib.load(os.path.join(MODEL_DIR, "mlb_ex.pkl"))
mlb_eq = joblib.load(os.path.join(MODEL_DIR, "mlb_eq.pkl"))

with open(os.path.join(ASSETS_DIR, "goal_mapping.json"), "r") as f:
    goal_mapping = json.load(f)

def predict_user(input_data_model):
    # Panggil fungsi preprocessing yang baru dengan argumen yang benar
    input_array = prepare_feature_array(input_data_model, scaler)

    # Prediksi Goal (tidak ada perubahan di sini)
    goal_pred = goal_model.predict(input_array)[0]
    goal_result = goal_mapping.get(str(goal_pred), "Unknown Goal")

    # Prediksi Multi-label (tidak ada perubahan di sini)
    multi_pred = multi_model.predict(input_array)[0]
    ex_len = len(mlb_ex.classes_)

    exercise_result = [mlb_ex.classes_[i] for i, val in enumerate(multi_pred[:ex_len]) if val == 1]
    equipment_result = [mlb_eq.classes_[i] for i, val in enumerate(multi_pred[ex_len:]) if val == 1]

    return {
        "Fitness Goal": goal_result,
        "Recommended Exercises": exercise_result,
        "Required Equipment": equipment_result
    }