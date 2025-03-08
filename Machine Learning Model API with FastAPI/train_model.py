import joblib
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Load dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Define features and target
X = df.drop(columns=["MedHouseVal"])  # Features
y = df["MedHouseVal"]  # Target variable

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a preprocessing + model pipeline
model_pipeline = Pipeline([
    ('scaler', StandardScaler()), 
    ('model', LinearRegression())  # You can replace this with any other model
])

# Train the model
model_pipeline.fit(X_train, y_train)

# Save the model
joblib.dump(model_pipeline, "models/model.pkl")

print("Model training complete. Saved as 'models/model.pkl'.")
