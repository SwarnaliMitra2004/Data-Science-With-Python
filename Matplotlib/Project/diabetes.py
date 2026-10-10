# Import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. LOAD THE DATA
# Read the CSV file into a DataFrame
data = pd.read_csv(
    r"D:\New folder\Matplotlib\Project\diabetes.csv"
)

# Display the first five rows
print(data.head())

# Display the number of rows and columns
print("Dataset shape:", data.shape)

# Display column names
print("Column names:", data.columns.tolist())

# Display data types and non-null values
data.info()

# Display statistical summary
print(data.describe())


# 2. DATA PREPROCESSING
# Check for missing values in each column
print("\nMissing values:")
print(data.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:", data.duplicated().sum())

# Remove duplicate rows, if any
data = data.drop_duplicates()

# Check the number of zero values in each column
# Some zero values may represent missing measurements
print("\nZero values in each column:")
print((data == 0).sum())

# In the common Pima dataset, zero values in these
# measurement columns may indicate missing measurements.
# Do not replace zeros in Pregnancies or Outcome.
measurement_columns = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

# Replace zero values in selected measurements with NaN
# so that they can be examined and handled as missing values
data[measurement_columns] = data[measurement_columns].replace(
    0, np.nan
)

# Display missing values after checking zero measurements
print("\nMissing values after zero-value check:")
print(data.isnull().sum())

# Fill missing numerical measurements with their median
# Median is less affected by extreme values than the mean
for column in measurement_columns:
    data[column] = data[column].fillna(data[column].median())

# Confirm that missing values have been handled
print("\nMissing values after filling:")
print(data.isnull().sum())



# 3. HANDLE CATEGORICAL DATA
# Outcome is the target category:
# 0 = no diabetes recorded
# 1 = diabetes recorded
print("\nOutcome counts:")
print(data["Outcome"].value_counts())

# Display the proportion of each outcome
print("\nOutcome proportions:")
print(data["Outcome"].value_counts(normalize=True))

# Convert Outcome to readable labels for visualization
data["Outcome_Label"] = data["Outcome"].map({
    0: "No Diabetes",
    1: "Diabetes"
})

# Display the updated dataset
print(data.head())


# 4. UNIVARIATE ANALYSIS
# Univariate analysis studies one variable at a time.

# 4.1 Distribution of Age
sns.histplot(data=data, x="Age", kde=True)
plt.title("Distribution of Age")
plt.show()

# 4.2 Distribution of Glucose
sns.histplot(data=data, x="Glucose", kde=True)
plt.title("Distribution of Glucose")
plt.show()

# 4.3 Distribution of BMI
sns.histplot(data=data, x="BMI", kde=True)
plt.title("Distribution of BMI")
plt.show()

# 4.4 Distribution of Insulin
sns.histplot(data=data, x="Insulin", kde=True)
plt.title("Distribution of Insulin")
plt.show()

# 4.5 Boxplot of Age to examine spread and potential outliers
sns.boxplot(y=data["Age"])
plt.title("Age Distribution - Boxplot")
plt.show()

# 4.6 Boxplot of Glucose
sns.boxplot(y=data["Glucose"])
plt.title("Glucose Distribution - Boxplot")
plt.show()

# 4.7 Countplot of the target variable
sns.countplot(data=data, x="Outcome_Label")
plt.title("Diabetes Outcome Count")
plt.xlabel("Outcome")
plt.show()


# 5. BIVARIATE ANALYSIS
# Bivariate analysis examines the relationship between two variables.

# 5.1 Glucose vs Outcome
# Compare glucose distributions for the two outcome groups
sns.boxplot(
    data=data,
    x="Outcome_Label",
    y="Glucose"
)
plt.title("Glucose by Diabetes Outcome")
plt.show()

# 5.2 BMI vs Outcome
sns.boxplot(
    data=data,
    x="Outcome_Label",
    y="BMI"
)
plt.title("BMI by Diabetes Outcome")
plt.show()

# 5.3 Age vs Outcome
sns.boxplot(
    data=data,
    x="Outcome_Label",
    y="Age"
)
plt.title("Age by Diabetes Outcome")
plt.show()

# 5.4 Glucose vs BMI
# Colors represent the diabetes outcome
sns.scatterplot(
    data=data,
    x="Glucose",
    y="BMI",
    hue="Outcome_Label"
)
plt.title("Glucose vs BMI")
plt.show()

# 5.5 Correlation heatmap
# Shows correlations between numerical variables
numeric_data = data.select_dtypes(include="number")

plt.figure(figsize=(10, 8))
sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    linewidths=1,
    fmt=".2f"
)
plt.title("Correlation Heatmap - Diabetes Dataset")
plt.show()