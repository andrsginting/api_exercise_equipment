# app/utils/download_model.py
import os
import gdown

def download_model():
    model_path = "app/models/multi_model.pkl"
    file_id = "1VY0y3NWpjXDXRLd8VlH7MYfXHdRJn3eN"  # ganti dengan ID Google Drive kamu
    url = f"https://drive.google.com/uc?id={file_id}"

    if not os.path.exists(model_path):
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        gdown.download(url, model_path, quiet=False)
