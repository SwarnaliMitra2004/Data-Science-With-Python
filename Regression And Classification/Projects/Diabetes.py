
import numpy as np
import pandas as pd

# Import the required libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load the diabetes dataset
df = pd.read_csv(r'D:\New folder\Matplotlib\Project\diabetes.csv')

# Display the first five rows
print("First five rows:")
print(df.head())

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display dataset information
print("\nDataset information:")
df.info()

# Select the input features
# All columns except Outcome are used for prediction
features = df.drop(columns=['Outcome']).values

# Select the target column
# 0 = Diabetes not indicated
# 1 = Diabetes indicated
label = df['Outcome'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    features,
    label,
    test_size=0.2,
    random_state=23,
    stratify=label
)

# Create a pipeline:
# 1. Fill missing values with column means
# 2. Standardize the features
# 3. Train the Logistic Regression model
model = make_pipeline(
    SimpleImputer(strategy='mean'),
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

# Train the model
model.fit(X_train, y_train)

# Display training and testing accuracy
print("\nTraining accuracy:", model.score(X_train, y_train))
print("Testing accuracy:", model.score(X_test, y_test))

# Predict the test-set results
y_pred = model.predict(X_test)

# Display the confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Display the classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Predict diabetes for a new patient
# Example values: pregnancies, glucose, blood pressure,
# skin thickness, insulin, BMI, diabetes pedigree function, age
new_patient = [[1, 120, 70, 20, 79, 25.0, 0.5, 30]]

prediction = model.predict(new_patient)

if prediction[0] == 1:
    print("\nPrediction: Diabetes indicated by the model.")
else:
    print("\nPrediction: Diabetes not indicated by the model.")