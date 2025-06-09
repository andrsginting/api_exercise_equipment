# app/utils/preprocessing.py
import numpy as np

def prepare_feature_array(user_input, scaler):
    """
    Menyiapkan array fitur dari data yang sudah divalidasi
    dan menerapkan normalisasi pada Height & Weight.
    """
    # Normalisasi Height & Weight menggunakan scaler yang sudah di-load
    height_weight_scaled = scaler.transform([[user_input.Height, user_input.Weight]])
    height, weight = height_weight_scaled[0]

    # Susun fitur sesuai urutan saat training model
    # Urutan: ['Sex', 'Age', 'Height', 'Weight', 'Hypertension', 'Diabetes']
    feature_array = np.array([
        user_input.Sex,
        user_input.Age,
        height,
        weight,
        user_input.Hypertension,
        user_input.Diabetes
    ]).reshape(1, -1)

    return feature_array