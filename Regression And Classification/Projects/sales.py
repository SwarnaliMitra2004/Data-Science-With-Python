
import numpy as np
import pandas as pd

# Import the required libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer

# Load the sales dataset
df = pd.read_csv(r'D:\New folder\Regression And Classification\Projects\sales.csv')

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
features = df.drop(columns=['Sales']).values

# Select the target column
label = df['Sales'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    features,
    label,
    test_size=0.2,
    random_state=23
)

# Create a pipeline to handle missing values
# and train the Linear Regression model
model = make_pipeline(
    SimpleImputer(strategy='mean'),
    LinearRegression()
)

# Train the model
model.fit(X_train, y_train)

# Display training and testing accuracy
print("\nTraining R2 score:", model.score(X_train, y_train))
print("Testing R2 score:", model.score(X_test, y_test))

# Predict the test-set results
y_pred = model.predict(X_test)

# Display evaluation metrics
print("\nMean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))