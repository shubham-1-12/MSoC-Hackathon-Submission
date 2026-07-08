import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    average_precision_score,
    classification_report,
    confusion_matrix
)

print("Loading dataset...")

df = pd.read_csv("data/creditcard.csv")

print(df.head())

X = df.drop("Class", axis=1)
y = df["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("Predicting...")

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
pr_auc = average_precision_score(y_test, y_prob)

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nPrecision :", precision)
print("Recall    :", recall)
print("F1 Score  :", f1)
print("PR AUC    :", pr_auc)

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/model.pkl")

with open("RESULTS.md", "w") as f:
    f.write(f"""# RESULTS

Precision: {precision:.4f}

Recall: {recall:.4f}

F1 Score: {f1:.4f}

PR-AUC: {pr_auc:.4f}
""")

print("\nModel saved successfully!")
print("Results saved!")