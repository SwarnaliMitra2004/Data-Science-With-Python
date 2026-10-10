
# Import NumPy for numerical operations
import numpy as np

# Import Pandas to work with tabular data
import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv(
    r'D:\New folder\Numpy and pandas\Topics to learn\50_Startups.csv'
)

# Display the first 5 rows of the dataset
print(df.head())

# Display column names, data types, and missing-value information
df.info()

# Remove rows containing missing values
df.dropna(inplace=True)

# Display statistical information about numerical columns
print(df.describe())

# Select the first column as the feature (X)
features = df.iloc[:, [0]].values

# Select the second column as the label (y)
label = df.iloc[:, [1]].values

# Import the function used to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Split the data: 80% for training and 20% for testing
# random_state=23 makes the split reproducible
X_train, X_test, y_train, y_test = train_test_split(
    features,
    label,
    test_size=0.2,
    random_state=23
)

# Import the Linear Regression algorithm
from sklearn.linear_model import LinearRegression

# Create a Linear Regression model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Check the model's R² score on the training data
print("Training score:", model.score(X_train, y_train))

# Display the coefficient (slope) learned by the model
print("Coefficient:", model.coef_)

# Display the intercept (starting value) learned by the model
print("Intercept:", model.intercept_)

# Check the model's performance on unseen testing data
print("Testing score:", model.score(X_test, y_test))
