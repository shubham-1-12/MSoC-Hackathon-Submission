# FraudShield AI

AI-Powered Credit Card Fraud Detection Dashboard

FraudShield AI is a machine learning web application developed for the MSoC 2026 Hackathon. It helps identify potentially fraudulent credit card transactions by analyzing uploaded transaction data and assigning a fraud prediction with a risk score.

---

## Team

**Team Name:** Draev Devs

**Members**
- Shubham Vishwakarma
- Tejas Shah

---

## Live Demo

**Application:** https://fraudshieldx.streamlit.app

---

## Features

- AI-powered fraud detection
- Batch CSV transaction analysis
- Fraud probability (Risk Score)
- Interactive Streamlit dashboard
- Downloadable prediction results
- Random Forest machine learning model
- Simple and intuitive interface

---

## Technology Stack

### Frontend
- Streamlit

### Backend
- Python

### Machine Learning
- Scikit-learn
- Random Forest Classifier

### Libraries
- Pandas
- NumPy
- Joblib

---

## Project Structure

```
FraudShield-AI/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
├── RESULTS.md
├── .gitignore
├── model.pkl
```

---

## How It Works

1. Upload a CSV file containing transaction data.
2. The application preprocesses the data.
3. The trained Random Forest model analyzes every transaction.
4. Fraud predictions and risk scores are generated.
5. Results can be downloaded as a CSV file.

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd FraudShield-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Dataset

The model was trained using the **Credit Card Fraud Detection Dataset** by the ULB Machine Learning Group and Worldline.

The dataset is **not included** in this repository due to licensing and file size considerations.

---

## Model Performance

| Metric | Score |
|---------|------:|
| Precision | 90.59% |
| Recall | 78.57% |
| F1 Score | 84.15% |
| PR-AUC | 86.29% |

---

## Future Improvements

- Real-time transaction monitoring
- Explainable AI (SHAP/LIME)
- REST API integration
- User authentication
- Dashboard analytics and charts
- Cloud database integration
- Multi-model ensemble learning

---

## License

This project was developed for educational and hackathon purposes.

---

## Developed By

**Draev Devs**

MSoC 2026 Hackathon
