# app/utils/download_model.py
import os
import gdown

def download_multi_model():
    """
    Mengecek dan men-download file multi_model.pkl jika belum ada.
    File ini berukuran besar dan tidak disimpan di repositori Git.
    """
    model_path = "app/models/multi_model.pkl"
    file_id = "1VY0y3NWpjXDXRLd8VlH7MYfXHdRJn3eN"  # ID Google Drive untuk multi_model.pkl

    # Cek jika file model sudah ada
    if not os.path.exists(model_path):
        print(f"File {model_path} not found. Downloading from Google Drive...")
        
        # Buat direktori 'app/models/' jika belum ada
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, model_path, quiet=False)
        print("Download complete.")
    else:
        print(f"File {model_path} already exists. Skipping download.")