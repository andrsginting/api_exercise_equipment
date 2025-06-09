# app/services/predictor.py
import joblib
import numpy as np
import json
import os
from app.utils.preprocessing import prepare_feature_array
from app.utils.download_model import download_multi_model # <-- Impor fungsi yang benar

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


# Sisa kode (fungsi predict_user) TIDAK PERLU diubah
def predict_user(input_data_model):
    # ...
    # ... (kode ini sudah benar)