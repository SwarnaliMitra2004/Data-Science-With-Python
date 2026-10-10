
import numpy as np
import pandas as pd

# Import the required libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv(r'Matplotlib/Topics to learn/Social_Network_Ads.csv')

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
# Age and EstimatedSalary are used to predict the purchase
features = df[['Age', 'EstimatedSalary']].values

# Select the target column
# 0 = Did not purchase, 1 = Purchased
label = df['Purchased'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    features,
    label,
    test_size=0.2,
    random_state=23,
    stratify=label
)

# Create a pipeline that scales the features
# and then trains the Logistic Regression model
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

# Train the model using the training data
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

# Predict whether a new customer will purchase
# Example: Age = 35, Estimated Salary = 60000
new_customer = [[35, 60000]]

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("\nPrediction: The customer is likely to purchase.")
else:
    print("\nPrediction: The customer is unlikely to purchase.")
