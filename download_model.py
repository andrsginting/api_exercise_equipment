import os
import gdown

# Ganti ini dengan ID file Google Drive kamu
file_id = "1i5o3sWF1dPbt-3rpGcMyBBGrZIPM6CeE"  # <--- UBAH DENGAN ID-MU SENDIRI
output_path = "app/models/multi_model.pkl"

# Cek apakah file sudah ada
if not os.path.exists(output_path):
    print("Model tidak ditemukan. Mengunduh dari Google Drive...")
    url = f"https://drive.google.com/uc?id={file_id}"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    gdown.download(url, output_path, quiet=False)
else:
    print("Model sudah tersedia.")
