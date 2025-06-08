from google_drive_downloader import GoogleDriveDownloader as gdd
import os

def download_model():
    model_path = "app/models/multi_model.pkl"
    if not os.path.exists(model_path):
        gdd.download_file_from_google_drive(
            file_id="1i5o3sWF1dPbt-3rpGcMyBBGrZIPM6CeE",  # ganti dengan ID Google Drive kamu
            dest_path=model_path,
            unzip=False
        )
