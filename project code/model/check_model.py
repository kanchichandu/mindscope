import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATA ----------------
data = pd.read_csv("StressLevelDataset.csv")

# Features and target
X = data.drop("stress_level", axis=1)
y = data["stress_level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL FILES ----------------
model_files = [
    "mental_health_model.pkl",
    "mental_health_model1.pkl",
    "mental_health_model2.pkl",
    "naive_bayes_model.pkl"
]

print("\n🔍 Checking Models...\n")

best_acc = 0
best_model = ""
best_algo = ""

# ---------------- CHECK EACH MODEL ----------------
for file in model_files:
    path = os.path.join("model", file)

    try:
        model = joblib.load(path)

        # Get algorithm name
        algo = model.__class__.__name__

        # Predict
        y_pred = model.predict(X_test)

        # Accuracy
        acc = accuracy_score(y_test, y_pred)

        print(f"{file} → {algo} → Accuracy: {acc:.4f}")

        # Track best model
        if acc > best_acc:
            best_acc = acc
            best_model = file
            best_algo = algo

    except Exception as e:
        print(f"{file} → ERROR: {e}")

# ---------------- BEST MODEL ----------------
print("\n🔥 Best Model:")
print(f"{best_model} → {best_algo} → Accuracy: {best_acc:.4f}")