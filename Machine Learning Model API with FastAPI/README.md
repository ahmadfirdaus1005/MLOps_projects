# **Machine Learning Model API with FastAPI**

This project creates an API for a machine learning model using FastAPI. The model is used to predict housing prices based on several features from the **California Housing Dataset**. The API is designed to allow users to interact with the model via a web interface (Swagger UI) and submit prediction requests.

---

## **📊 About the Dataset**

The dataset used in this project is the **California Housing Dataset**, which is available in the `sklearn.datasets` module. It contains information about various features of houses in California and is used to predict the median house value for California districts.

### **Features:**
The dataset includes the following features:

1. **MedInc (Median Income):** The median income in a block group.
2. **HouseAge:** The median age of the houses in the block group.
3. **AveRooms:** The average number of rooms per household.
4. **AveBedrms:** The average number of bedrooms per household.
5. **Population:** The population of the block group.
6. **AveOccup:** The average number of people per household.
7. **Latitude:** The latitude of the district.
8. **Longitude:** The longitude of the district.

### **Target Variable:**
- **MedianHouseValue (Prediction Target):** The median house value for a district, which is the target variable for this prediction model.

The dataset contains a large number of data points (about 20,000 rows) and is typically used in regression problems, where the goal is to predict a continuous value (in this case, the median house value).

---

## 🔧 Project Setup
Prerequisites:
Make sure you have Python installed. You can download Python from here.

### 1. Clone the Repository:
First, clone the repository to your local machine:
```sh
git clone https://github.com/ahmadfirdaus1005/fastapi-ml-model-api.git

cd fastapi-ml-model-api
```
### 2. Install Dependencies:
Navigate into the project directory and install the required dependencies:
```sh
pip install -r requirements.txt

```

The requirements.txt file includes the necessary packages such as:
- `fastapi`
- `uvicorn`
- `scikit-learn`
- `pydantic`

### 3. Run the Application:
To start the FastAPI server, run the following command:
```sh
uvicorn app.main:app --reload
```
This will start the server locally at http://127.0.0.1:8000

##  🌐 How to Use Swagger UI
Once the `Fast API` server is running, you can interact with the API using `Swagger UI`.

1. Open Swagger UI:
   Open your web browser and navigate to the following URL:
   ```sh
   http://127.0.0.1:8000/docs
   ```
2. Submit Prediction Request:
   - Scroll down to the POST /predict section in the `Swagger UI`.
   - Click on "Try it out".
   - Enter the input data in `JSON format`, for example:
   ```sh
   {
   "MedInc": 5.6,
   "HouseAge": 15,
   "AveRooms": 6,
   "AveBedrms": 1,
   "Population": 1500,
   "AveOccup": 3,
   "Latitude": 34.2,
   "Longitude": -118.5}
   ```
## ✨ Additional Information
Feel free to customize and extend this project. You can add additional models, deploy it using Docker, or host it on cloud platforms like Heroku or AWS.

