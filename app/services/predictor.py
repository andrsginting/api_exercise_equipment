# app/services/predictor.py
import joblib
import numpy as np
import json
import os
from app.utils.preprocessing import prepare_feature_array
from download_model import download_multi_model # <-- Impor fungsi yang benar

# ====================================================================
# LANGKAH 1: PASTIKAN MODEL BESAR (multi_model.pkl) SUDAH DI-DOWNLOAD
download_multi_model()
# ====================================================================


# LANGKAH 2: Load SEMUA model.
# - multi_model.pkl akan di-load dari hasil download.
# - File .pkl lainnya akan di-load dari repositori Git.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

print("Loading models...")
goal_model = joblib.load(os.path.join(MODEL_DIR, "goal_model.pkl"))
multi_model = joblib.load(os.path.join(MODEL_DIR, "multi_model.pkl")) # Ini sekarang PASTI ada
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
mlb_ex = joblib.load(os.path.join(MODEL_DIR, "mlb_ex.pkl"))
mlb_eq = joblib.load(os.path.join(MODEL_DIR, "mlb_eq.pkl"))

with open(os.path.join(ASSETS_DIR, "goal_mapping.json"), "r") as f:
    goal_mapping = json.load(f)
print("Models loaded successfully.")

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
        "fitnessGoal": goal_result,
        "recommendedExercises": exercise_result,
        "requiredEquipment": equipment_result
    }