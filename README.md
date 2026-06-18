# 🏦 Loan Approval Prediction System

An interactive machine learning web application built with **Streamlit** that evaluates applicant details and predicts whether a loan will be approved or rejected.

---

## 📖 Overview
This project takes a user's financial and demographic information and runs it through a pre-trained scikit-learn machine learning pipeline to determine loan eligibility. It provides a clean, user-friendly interface for immediate predictions and also displays the probability of approval.

---

## 🛠️ Setup & Local Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Parul2007/Loan-Approval-ML-Model.git
cd Loan-Approval-ML-Model
```

### 2. Create a Virtual Environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App Locally
```bash
streamlit run app.py
```

---

## 📋 Required Details for Prediction
To get a loan prediction, you will need to provide the following details in the web application:

1. **Gender:** Male or Female.
2. **Married:** Yes or No.
3. **Dependents:** Number of dependents (0, 1, 2, 3+, or 4).
4. **Education:** Graduate or Not Graduate.
5. **Self Employed:** Yes or No.
6. **Applicant Income:** The primary applicant's monthly income.
7. **Coapplicant Income:** The co-applicant's monthly income (enter 0 if none).
8. **Loan Amount:** The total loan amount requested.
9. **Loan Amount Term:** The duration of the loan in months (120, 180, 240, or 360).
10. **Credit History:** 1 for good credit history, 0 for bad/no credit history.
11. **Property Area:** Urban, Semiurban, or Rural.

Once filled out, simply click **Predict** to see if the loan is Approved or Rejected!

---

## 🚀 How to Deploy on Streamlit Community Cloud (Recommended)
Since this app is built with Streamlit, the easiest and most reliable way to host it is on **Streamlit Community Cloud** (it is completely free!). 

Follow these steps to deploy your app to the internet:

1. Push your code to your GitHub repository (already done!).
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and sign up / log in with your **GitHub account**.
3. Once logged in, click the **"New app"** button.
4. Fill in the following details:
   - **Repository:** `Parul2007/Loan-Approval-ML-Model`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **Deploy!**

It will take a minute or two to install the requirements on their servers. Once finished, your app will be live and you will get a public URL that you can share with anyone!
