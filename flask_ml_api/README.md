# Flask ML API

This project is a simple machine learning API built using Flask. It serves a trained Random Forest model to predict house prices based on the California housing dataset.

## Features
- Train a machine learning model using `RandomForestRegressor`.
- Save and load the model using `joblib`.
- Serve the model using Flask API.
- Accepts input via JSON and returns predictions.

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/ahmadfirdaus1005/flask-ml-api.git
cd flask-ml-api
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Train and Save the Model
Run the following script to train the model and save it:
```sh
python train_model.py
```

### 5. Run the Flask API
```sh
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

## API Endpoints

### 1. Health Check
```sh
GET /
```
**Response:**
```json
{"message": "API is running!"}
```

### 2. Predict House Price
```sh
POST /predict
```
**Request Body (JSON):**
```json
{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984127,
    "AveBedrms": 1.02381,
    "Population": 322.0,
    "AveOccup": 2.555556,
    "Latitude": 37.88,
    "Longitude": -122.23
}
```
**Response:**
```json
{"prediction": [4.2321]}
```

## Testing the API

Run the following command to test the API:
```sh
python test_request.py
```

## Folder Structure
```
flask_ml_api/
│── model/               # Stores trained model and scaler
│   ├── model.pkl
│   ├── scaler.pkl
│── app.py               # Flask API script
│── train_model.py        # Train and save the ML model
│── test_request.py       # Script to test the API
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```

## License
This project is open-source under the MIT License.

---

