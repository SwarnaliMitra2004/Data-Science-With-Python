
import numpy as np
import pandas as pd

# Import the required libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv(
    r'D:\New folder\Regression And Classification\Topics To Learn\cancer.csv'
)

# Display basic information about the dataset
print("First five rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

# Check that the expected target column exists
target_column = 'SeriousDlqin2yrs'

if target_column not in df.columns:
    raise ValueError(
        f"Target column '{target_column}' was not found. "
        "Check the printed column names and select the correct target."
    )

# Separate features and target
features = df.drop(columns=[target_column])
label = df[target_column]

# Convert feature columns to numeric values where possible
features = features.apply(pd.to_numeric, errors='coerce')

# Remove rows where the target is missing
valid_rows = label.notna()
features = features.loc[valid_rows]
label = label.loc[valid_rows]

# Remove rows with invalid target values
valid_classes = label.isin([0, 1])
features = features.loc[valid_classes]
label = label.loc[valid_classes].astype(int)

# Check the target classes
print("\nTarget class counts:")
print(label.value_counts())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    features,
    label,
    test_size=0.2,
    random_state=23,
    stratify=label
)

# Build a pipeline:
# 1. Fill missing feature values with their column means
# 2. Standardize feature scales
# 3. Train the Logistic Regression model
model = make_pipeline(
    SimpleImputer(strategy='mean'),
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

# Train the model
model.fit(X_train, y_train)

# Calculate accuracy
print("\nTraining accuracy:", model.score(X_train, y_train))
print("Testing accuracy:", model.score(X_test, y_test))

# Predict the test-set labels
y_pred = model.predict(X_test)

# Display the confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Display precision, recall, F1-score and support
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
