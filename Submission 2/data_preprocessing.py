import joblib
import numpy as np
import pandas as pd

encoder_Tuition_fees_up_to_date = joblib.load("model/Tuition_fees_up_to_date_encoder.joblib")
encoder_Scholarship_holder = joblib.load("model/Scholarship_holder_encoder.joblib")
encoder_Debtor = joblib.load("model/Debtor_encoder.joblib")
encoder_Displaced = joblib.load("model/Displaced_encoder.joblib")
encoder_Daytime_evening_attendance = joblib.load("model/Daytime_evening_attendance_encoder.joblib")
encoder_Gender = joblib.load("model/Gender_encoder.joblib")

scaler_Admission_grade = joblib.load("model/Admission_grade_scaler.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/Curricular_units_1st_sem_approved_scaler.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model/Curricular_units_1st_sem_credited_scaler.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/Curricular_units_1st_sem_enrolled_scaler.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/Curricular_units_1st_sem_grade_scaler.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/Curricular_units_2nd_sem_approved_scaler.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model/Curricular_units_2nd_sem_credited_scaler.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/Curricular_units_2nd_sem_enrolled_scaler.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/Curricular_units_2nd_sem_grade_scaler.joblib")
scaler_Previous_qualification_grade = joblib.load("model/Previous_qualification_grade_scaler.joblib")

def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    # Perform encode
    df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.transform(data["Tuition_fees_up_to_date"])
    df["Scholarship_holder"] = encoder_Scholarship_holder.transform(data["Scholarship_holder"])
    df["Debtor"] = encoder_Debtor.transform(data["Debtor"])
    df["Displaced"] = encoder_Displaced.transform(data["Displaced"])
    df["Daytime_evening_attendance"] = encoder_Daytime_evening_attendance.transform(data["Daytime_evening_attendance"])
    df["Gender"] = encoder_Gender.transform(data["Gender"])

    # Perform scaling
    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1, 1))
    df["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1, 1))
    df["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1, 1))
    df["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1, 1))
    df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1, 1))
    df["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1, 1))
    df["Curricular_units_2nd_sem_credited"] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(data["Curricular_units_2nd_sem_credited"]).reshape(-1, 1))
    df["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1, 1))
    df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1, 1))
    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1, 1))
    
    return df