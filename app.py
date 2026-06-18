import streamlit as st
import pandas as pd
import joblib
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Approval Prediction System")

st.markdown(
    "Fill the applicant details below and predict loan approval."
)

model=joblib.load("models/loan_approval_pipeline.pkl")

st.title("Loan Approval Prediction")

gender=st.selectbox(
    "Gender",
    ["Male", "Female"]
)

married=st.selectbox(
    "Married",
    ["Yes","No"]
)

dependents=st.selectbox(
    "Dependents",
    ["0","1","2","3+","4"]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0
)

loan_term = st.selectbox(
    "Loan Amount Term",
    [120, 180, 240, 360]
)

credit_history = st.selectbox(
    "Credit History",
    [0, 1]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Rural", "Semiurban"]
)
input_data = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [dependents],
    "Education": [education],
    "Self_Employed": [self_employed],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_term],
    "Credit_History": [credit_history],
    "Property_Area": [property_area]
})

if st.button("Predict"):
    prediction = model.predict(
    input_data
)
    probability = model.predict_proba(
    input_data
)
    approval_probability = probability[0][1]

    st.write(
     f"Approval Probability: {approval_probability:.2%}"
)
    
    if prediction[0] == 1:
        st.success(
    "✅ Loan Approved"
)
    else:
        st.error(
        "❌Loan Rejected"
    )