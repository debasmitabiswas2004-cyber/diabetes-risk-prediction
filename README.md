# Diabetes Risk Prediction App

A machine learning web application built with **Python**, **Streamlit**, and a **Random Forest Classifier** to predict the likelihood of diabetes based on patient health parameters.

## Project Overview

This project predicts whether a person is likely to be diabetic based on medical input features such as glucose level, blood pressure, insulin, BMI, age, and other health-related parameters. The application uses a trained **Random Forest Classifier** and provides both the prediction result and the corresponding probability scores.

The model is based on the **Pima Indians Diabetes Dataset** and is deployed as an interactive **Streamlit web application**.

## Features

* Predicts diabetes risk using a trained Random Forest model
* User-friendly Streamlit interface for entering patient details
* Displays:

  * Prediction result (**likely diabetic / likely not diabetic**)
  * Probability of diabetes
  * Probability of no diabetes
* Includes a disclaimer for educational use
* Easy to run locally and can be deployed online

## Input Parameters

The app uses the following health parameters:

* **Number of Pregnancies**
* **Fasting Plasma Glucose Concentration (mg/dL)**
* **Diastolic Blood Pressure (mm Hg)**
* **Triceps Skin Fold Thickness (mm)**
* **2-Hour Serum Insulin (mu U/ml)**
* **Body Mass Index (BMI) (kg/m²)**
* **Diabetes Pedigree Function**
* **Age (years)**

## Tech Stack

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **Joblib**
* **NumPy**

## Project Structure

```bash
diabetes-risk-prediction/
│
├── app.py
├── README.md
├── requirements.txt
└── models/
    ├── diabetes_rf_model.pkl
    └── feature_columns.pkl
```

## How to Run the App Locally

### 1. Clone the repository
```bash
git clone https://github.com/debasmitabiswas2004-cyber/diabetes-risk-prediction.git
cd diabetes-risk-prediction
```

### 2. Install the required dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
python -m streamlit run app.py
```

## Model Information

* **Algorithm Used:** Random Forest Classifier
* **Dataset Used:** Pima Indians Diabetes Dataset
* **Target:** Predict whether a person is diabetic or not based on diagnostic measurements

## Live Demo
[Click here to use the app](https://diabetes-risk-prediction-db.streamlit.app/)

## Disclaimer

This application is built for **educational purposes only** and should **not** be used as a substitute for professional medical advice, diagnosis, or treatment.

## Future Improvements

* Deploy the application publicly using Streamlit Community Cloud
* Improve UI design and styling
* Add model performance metrics and visualizations
* Compare multiple machine learning algorithms
* Add input validation and better error handling

## Author

**Debasmita Biswas**
