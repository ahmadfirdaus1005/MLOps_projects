from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

# Initialize FastAPI app
app = FastAPI(title="ML Model API", description="API for ML Model Predictions", version="1.0")

# Define request model
class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the ML Model API!"}

# Prediction endpoint
@app.post("/predict")
def make_prediction(data: InputData):
    """Receives input JSON and returns the model prediction."""
    # input_dict = data.dict()
    input_dict = data.model_dump()  # Use model_dump() instead of dict()
    prediction = predict(input_dict)
    return {"prediction": prediction}
