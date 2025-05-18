import joblib

model = joblib.load("model/logistic_model.joblib")
result_target = joblib.load("model/target_encoder.joblib")

def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (Drop Out or Graduate)
    """
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)
    return final_result