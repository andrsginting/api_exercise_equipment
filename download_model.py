import os
import gdown


file_id = "1i5o3sWF1dPbt-3rpGcMyBBGrZIPM6CeE"  # ID dari multi_model.pkl
output_path = "app/models/multi_model.pkl"

if not os.path.exists(output_path):
    print("multi_model.pkl tidak ditemukan. Mengunduh dari Google Drive...")
    url = f"https://drive.google.com/uc?id={file_id}"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    gdown.download(url, output_path, quiet=False)
else:
    print("multi_model.pkl sudah tersedia.")
