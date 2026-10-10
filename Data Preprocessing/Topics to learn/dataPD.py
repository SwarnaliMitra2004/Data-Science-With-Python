
import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv(
    r'D:\New folder\Data Preprocessing\Topics to learn\melb_data.csv'
)

# 2. Inspect the dataset
df.info()

# 3. Handle missing continuous numerical values using mean
continuous_columns = [
    "Distance", "Landsize", "BuildingArea",
    "Lattitude", "Longtitude", "Propertycount"
]

for column in continuous_columns:
    df[column] = df[column].fillna(
        round(df[column].mean(), 2)
    )

# 4. Handle missing discrete numerical values using median
discrete_columns = [
    "Bedroom2", "Bathroom", "Car", "YearBuilt"
]

for column in discrete_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )

# 5. Handle missing categorical values using mode
categorical_columns = df.select_dtypes(
    include="object"
).columns

for column in categorical_columns:
    df[column] = df[column].fillna(
        df[column].mode()[0]
    )

# 6. Check missing values
print(df.isnull().sum())

# 7. Separate features and label
features = df.drop("Price", axis=1)
label = df["Price"]

# 8. Select categorical feature columns
categorical_columns = features.select_dtypes(
    include="object"
).columns

# 9. Convert categorical data into dummy variables
encoded_data = pd.get_dummies(
    features[categorical_columns],
    dtype=int
)

print(encoded_data.head())

# 10. Select numerical features
numerical_data = features.drop(
    columns=categorical_columns
)

# 11. Combine numerical and encoded categorical data
final_features = pd.concat(
    [numerical_data, encoded_data],
    axis=1
)

# 12. Display results
print(final_features.head())
print("Features shape:", final_features.shape)
print("Label shape:", label.shape)