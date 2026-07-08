# Smart Credit Card Fraud Investigation

## MSoC 2026 Hackathon Submission

### Team: Draev Devs

Team Members:
- Shubham Vishwakarma
- Tejas Shah

---

## Overview

Smart Credit Card Fraud Investigation is a machine learning-based fraud detection system designed to identify suspicious credit card transactions and assist investigators through automated risk scoring.

The system analyzes transaction patterns, predicts whether a transaction is fraudulent, and assigns a risk score to help prioritize investigation.

---

## Problem Statement

Credit card fraud is a continuously evolving problem. Traditional rule-based detection systems struggle to identify new fraud patterns and often generate a high number of false positives.

The objective of this project is to build an intelligent fraud detection pipeline that can:

- Detect fraudulent transactions accurately.
- Reduce false positive rates.
- Generate risk scores for transaction prioritization.
- Provide an easy-to-use investigation dashboard.

---

## Key Features

- Machine learning based fraud classification.
- Random Forest classification model.
- Continuous risk score generation (0-100).
- CSV-based batch transaction analysis.
- Streamlit-based interactive dashboard.
- Model evaluation and performance reporting.
- Retrainable ML pipeline.

---

## Technology Stack

Programming Language:
- Python

Libraries:
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

Machine Learning:
- Random Forest Classifier

---

## Project Structure

```
Fraud-Detection/
│
├── app.py                 # Streamlit dashboard
├── train.py               # Model training pipeline
├── requirements.txt       # Dependencies
├── RESULTS.md             # Model evaluation results
├── README.md
│
├── model/
│   └── model.pkl          # Trained model
│
└── data/
    └── creditcard.csv     # Dataset (download separately)
```

---

## Dataset

Dataset Used:

Credit Card Fraud Detection Dataset  
Source: Kaggle - ULB Machine Learning Group and Worldline

The dataset is not included in this repository due to GitHub file size limitations.

To run the project:

1. Download the dataset.
2. Place the file at:

```
data/creditcard.csv
```

Dataset Details:

- 284,807 transactions
- 30 input features
- Binary classification problem
- Highly imbalanced fraud distribution

---

## Machine Learning Approach

### Model

Random Forest Classifier

### Reason for Selection

Random Forest was selected because:

- It performs well on tabular datasets.
- It handles complex feature relationships.
- It provides reliable classification performance.
- It supports fast inference.

---

## Model Performance

Evaluation was performed on a held-out test dataset.

| Metric | Score |
|---|---:|
| Precision | 90.59% |
| Recall | 78.57% |
| F1 Score | 84.15% |
| PR-AUC | 86.29% |

Confusion Matrix:

| | Predicted Legitimate | Predicted Fraud |
|-|-:|-:|
| Actual Legitimate | 56856 | 8 |
| Actual Fraud | 21 | 77 |

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train.py
```

### Run the Dashboard

```bash
python -m streamlit run app.py
```

---

## Dashboard Workflow

1. Upload transaction CSV file.
2. System processes transaction features.
3. Machine learning model predicts fraud probability.
4. Dashboard displays:
   - Fraud prediction
   - Risk score
   - Transaction analysis

---

## Future Improvements

Future versions can include:

- Explainable AI using SHAP/LIME.
- Real-time fraud detection API.
- Graph-based fraud ring detection.
- Cloud deployment.
- Continuous model retraining.
- Advanced anomaly detection techniques.

---

## License

This project was developed for educational and hackathon purposes.