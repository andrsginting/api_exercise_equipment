# app/utils/preprocessing.py
def preprocess_input(user_input, scaler):
    sex = 0 if user_input['Sex'].lower() == 'male' else 1
    hyper = 1 if user_input['Hypertension'].lower() == 'yes' else 0
    diabetes = 1 if user_input['Diabetes'].lower() == 'yes' else 0

    height_weight_scaled = scaler.transform([[user_input['Height'], user_input['Weight']]])
    height, weight = height_weight_scaled[0]

    return [sex, user_input['Age'], height, weight, hyper, diabetes]
