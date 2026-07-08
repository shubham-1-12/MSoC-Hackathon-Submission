import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model.pkl")   # Change to "model.pkl" if your file is in root

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🛡️ FraudShield AI")

    st.markdown("---")

    st.markdown("""
### Smart Credit Card Fraud Investigation

Upload a CSV file containing transaction data.

The AI model will:

- Detect fraudulent transactions
- Calculate risk scores
- Generate prediction results
""")

    st.markdown("---")

    st.success("Model: Random Forest")
    st.info("Hackathon Project")

# -----------------------------
# Main Header
# -----------------------------
st.title("🛡️ FraudShield AI")
st.caption("AI-Powered Credit Card Fraud Detection Dashboard")

st.divider()

uploaded = st.file_uploader(
    "Upload Transaction CSV",
    type=["csv"]
)

if uploaded:

    with st.spinner("Loading dataset..."):
        df = pd.read_csv(uploaded)

    st.success("Dataset Loaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    if "Class" in df.columns:
        X = df.drop("Class", axis=1)
    else:
        X = df

    st.divider()

    if st.button("Predict Fraud", use_container_width=True):

        with st.spinner("Analyzing Transactions..."):

            pred = model.predict(X)
            prob = model.predict_proba(X)[:, 1]

        result = df.copy()
        result["Prediction"] = pred
        result["Risk Score (%)"] = (prob * 100).round(2)

        fraud = int((pred == 1).sum())
        total = len(result)
        fraud_rate = (fraud / total) * 100

        st.success("Analysis Completed Successfully")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Transactions",
            total
        )

        col2.metric(
            "Fraud Detected",
            fraud
        )

        col3.metric(
            "Fraud Rate",
            f"{fraud_rate:.2f}%"
        )

        st.divider()

        st.subheader("Prediction Results")

        st.dataframe(
            result,
            use_container_width=True
        )

        csv = result.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Results",
            data=csv,
            file_name="fraud_predictions.csv",
            mime="text/csv",
            use_container_width=True
        )

else:
    st.info("Upload a CSV file to begin fraud analysis.")

st.divider()

st.caption(
    "Developed by Draev Devs • MSoC 2026 Hackathon Submission"
)
