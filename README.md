# Diabetes Prediction App

A machine learning web application built with **Python**, **Streamlit**, and a **Random Forest Classifier** to predict the likelihood of diabetes based on patient health parameters.

## Features
- Predicts diabetes risk using a trained Random Forest model
- User-friendly Streamlit web interface
- Accepts medical inputs such as:
  - Number of Pregnancies
  - Fasting Plasma Glucose Concentration
  - Diastolic Blood Pressure
  - Triceps Skin Fold Thickness
  - 2-Hour Serum Insulin
  - Body Mass Index (BMI)
  - Diabetes Pedigree Function
  - Age
- Displays:
  - Prediction result
  - Probability of diabetes
  - Probability of no diabetes

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

## Dataset
This project uses the **Pima Indians Diabetes Dataset**.

## Project Structure
diabetes-risk-prediction/
│── data/
│── models/
│── notebooks/
│── src/
│── app.py
│── README.md
│── requirements.txt

## How to Run Locally
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the app :
   ```bash
   python -m streamlit run app.py

## Disclaimer
This application is for **educational purposes only** and should not be used as a substitute for professional medical diagnosis.