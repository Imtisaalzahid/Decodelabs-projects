# ================================
# Project 2: Data Classification Using AI
# ================================

# Import libraries
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------
# Step 1: Load Dataset
# --------------------------------

iris = load_iris()

# Convert dataset into DataFrame
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["Species"] = iris.target

print("First 5 Rows:\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------
# Step 2: Define Features and Target
# --------------------------------

X = iris.data
y = iris.target

# --------------------------------
# Step 3: Split Dataset
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# --------------------------------
# Step 4: Train AI Model
# --------------------------------

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# --------------------------------
# Step 5: Make Predictions
# --------------------------------

predictions = model.predict(X_test)

# --------------------------------
# Step 6: Evaluate Model
# --------------------------------

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

# --------------------------------
# Step 7: Confusion Matrix
# --------------------------------

cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    cmap="Blues",
    fmt="d",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# --------------------------------
# Step 8: Predict New Flower
# --------------------------------

new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

print("\nPredicted Flower:", iris.target_names[prediction][0])