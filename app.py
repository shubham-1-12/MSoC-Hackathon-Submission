import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Fraud Detection", layout="wide")

st.title("Smart Credit Card Fraud Investigation")

model = joblib.load("model.pkl")

uploaded = st.file_uploader("Upload creditcard.csv", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)

    st.subheader("Uploaded Data")
    st.dataframe(df.head())

    if "Class" in df.columns:
        X = df.drop("Class", axis=1)
    else:
        X = df

    if st.button("Predict Fraud"):
        pred = model.predict(X)
        prob = model.predict_proba(X)[:,1]

        result = df.copy()
        result["Prediction"] = pred
        result["Risk Score"] = (prob*100).round(2)

        st.subheader("Prediction Results")
        st.dataframe(result)

        fraud = (pred==1).sum()

        st.metric("Fraudulent Transactions", fraud)
