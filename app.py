import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("models/diabetes_rf_model.pkl")

# -----------------------------
# App title and description
# -----------------------------
st.title("🩺 Diabetes Prediction App")
st.write("Enter the patient details below to estimate diabetes risk using a trained Random Forest model.")

st.caption(
    "This project uses the Pima Indians Diabetes dataset. "
    "In this dataset, blood pressure is represented as **Diastolic Blood Pressure (mm Hg)**."
)

# -----------------------------
# User input fields
# -----------------------------
pregnancies = st.number_input(
    "Number of Pregnancies",
    min_value=0,
    max_value=20,
    value=1,
    step=1
)

glucose = st.number_input(
    "Fasting Plasma Glucose Concentration (mg/dL)",
    min_value=0,
    max_value=300,
    value=120,
    step=1
)

blood_pressure = st.number_input(
    "Diastolic Blood Pressure (mm Hg)",
    min_value=0,
    max_value=200,
    value=70,
    step=1
)

skin_thickness = st.number_input(
    "Triceps Skin Fold Thickness (mm)",
    min_value=0,
    max_value=100,
    value=20,
    step=1
)

insulin = st.number_input(
    "2-Hour Serum Insulin (µU/mL)",
    min_value=0,
    max_value=900,
    value=79,
    step=1
)

bmi = st.number_input(
    "Body Mass Index (kg/m²)",
    min_value=0.0,
    max_value=70.0,
    value=25.0,
    step=0.1
)

dpf = st.number_input(
    "Diabetes Pedigree Function (score)",
    min_value=0.0,
    max_value=3.0,
    value=0.5,
    step=0.01
)

age = st.number_input(
    "Age (years)",
    min_value=1,
    max_value=120,
    value=30,
    step=1
)

# -----------------------------
# Prediction button
# -----------------------------
if st.button("Predict Diabetes Risk"):
    input_data = pd.DataFrame([{
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ The model predicts that the person is **likely diabetic**.")
    else:
        st.success("✅ The model predicts that the person is **likely not diabetic**.")

    st.write(f"**Probability of No Diabetes:** {probability[0] * 100:.2f}%")
    st.write(f"**Probability of Diabetes:** {probability[1] * 100:.2f}%")

# -----------------------------
# Disclaimer
# -----------------------------
st.warning(
    "This application is for educational purposes only and should not be used as a substitute for professional medical diagnosis."
)