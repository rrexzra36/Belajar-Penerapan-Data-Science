import os
import joblib

def load_model(filename):
    return joblib.load(os.path.join(os.path.dirname(__file__), "model", filename))

model = load_model("logistic_model.joblib")
result_target = load_model("target_encoder.joblib")

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