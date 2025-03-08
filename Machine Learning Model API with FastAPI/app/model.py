import joblib
import numpy as np
import pandas as pd
from pathlib import Path

# Load the model
MODEL_PATH = Path(__file__).parent / "../models/model.pkl"
model = joblib.load(MODEL_PATH)

def predict(features: dict):
    """Make a prediction using the trained model."""
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    return prediction[0]
