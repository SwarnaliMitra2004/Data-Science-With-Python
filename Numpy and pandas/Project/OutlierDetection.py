import pandas as pd

# Load the dataset
df = pd.read_csv("datasetExample.csv")

# Display the dataset
print("Dataset:")
print(df)

# Detect outliers in numerical columns using IQR
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower_limit) |
                  (df[column] > upper_limit)]

    print(f"\nOutliers in {column}:")
    print(outliers[column])