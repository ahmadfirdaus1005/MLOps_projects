# 🏡 House Price Prediction with MLflow Tracking

This project builds a **house price prediction model** using the California Housing dataset and tracks experiments using **MLflow**. The model is trained using a **Random Forest Regressor**, and hyperparameter tuning is performed using **GridSearchCV**. All relevant metrics, parameters, and models are logged via MLflow.

---

## 📦 Requirements

Make sure you have the following installed:

- Python 3.7+
- pip
- virtualenv (optional but recommended)
- MLflow
- scikit-learn
- pandas

You can install all dependencies with:

```bash
pip install -r requirements.txt
```
---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/ahmadfirdaus1005/MLOps_projects.git
cd MLOps_projects/ml_project_with_mlflow_tracking
```
### 2. Start MLflow Tracking Server (on localhost)
```bash
mlflow ui
```
This will launch the MLflow UI at: http://127.0.0.1:5000

### 3. Run the Training Script
Run the Jupyter Notebook or Python script that contains the training code:
```bash
jupyter notebook housePredictionModel.ipynb
```
