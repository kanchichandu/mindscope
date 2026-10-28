import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("StressLevelDataset.csv")

# Features and target
X = data.drop("stress_level", axis=1)   # change if column name is different
y = data["stress_level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Naive Bayes Accuracy:", acc)

# Save model
joblib.dump(model, "model/naive_bayes_model.pkl")