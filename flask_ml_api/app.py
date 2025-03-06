from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/")
def home():
    return "Welcome to the ML API! Use the /predict endpoint."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Ensure all required features are provided
        required_features = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
        if not all(feature in data for feature in required_features):
            return jsonify({"error": "Missing required features"}), 400

        # Convert input into a NumPy array
        input_data = np.array([[data[feature] for feature in required_features]])

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)

        # Return response
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
