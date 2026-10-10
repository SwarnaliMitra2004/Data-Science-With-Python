
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# 1. Load the dataset
df = pd.read_csv(
    r'D:\New folder\Data Preprocessing\Topics to learn\melb_data.csv'
)

# 2. Inspect the dataset
print(df.head())
df.info()

# 3. Separate features and label
features = df.drop("Price", axis=1)
label = df["Price"]

# 4. Select numerical feature columns
numerical_columns = features.select_dtypes(
    include=np.number
).columns

# 5. Apply SimpleImputer with mean strategy
imputer = SimpleImputer(strategy="mean")
features[numerical_columns] = imputer.fit_transform(
    features[numerical_columns]
)

# 6. Check missing numerical values
print(features[numerical_columns].isnull().sum())

# 7. Select categorical columns
categorical_columns = features.select_dtypes(
    include="object"
).columns

# 8. Fill missing categorical values with the mode
for column in categorical_columns:
    features[column] = features[column].fillna(
        features[column].mode()[0]
    )

# 9. Apply OneHotEncoder
encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

encoded_data = encoder.fit_transform(
    features[categorical_columns]
)

# 10. Convert encoded data into a DataFrame
encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out(categorical_columns),
    index=features.index
)

# 11. Keep numerical data separately
numerical_data = features.drop(columns=categorical_columns)

# 12. Combine numerical and encoded categorical data
final_features = np.concatenate(
    [
        numerical_data.to_numpy(),
        encoded_data
    ],
    axis=1
)

# 13. Display the results
print("Final features shape:", final_features.shape)
print(final_features[:5,:10])
print("Label shape:", label.shape)
