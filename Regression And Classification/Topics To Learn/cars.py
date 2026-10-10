
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

# Load dataset
df = pd.read_csv(
    r'D:\New folder\Numpy and pandas\Topics to learn\cars.csv'
)

# Replace '?' with NaN
df.replace('?', np.nan, inplace=True)

# Convert horsepower to numeric
df['horsepower'] = pd.to_numeric(
    df['horsepower'], errors='coerce'
)

# Features and label
features = df.drop(columns=['mpg', 'car name']).copy()
label = df['mpg'].values

# Separate numerical and categorical features
numeric_cols = [
    'cylinders', 'displacement', 'horsepower',
    'weight', 'acceleration', 'model year'
]

categorical_cols = ['origin']

# Extract numerical features
numeric_features = features[numeric_cols].values

# Create and instantiate the imputer
imputer = SimpleImputer(
    strategy='mean',
    missing_values=np.nan
)

# Fit and transform numerical features
numeric_features = imputer.fit_transform(numeric_features)

# One Hot Encoding
oh = OneHotEncoder(sparse_output=False)

origin = oh.fit_transform(features[categorical_cols])

# Combine encoded and numerical features
final_set = np.concatenate(
    (origin, numeric_features),
    axis=1
)

print("Final feature set:")
print(final_set)

print("\nLabel:")
print(label)

# Feature Scaling - StandardScaler
sc = StandardScaler()
feat_standard_scaler = sc.fit_transform(final_set)

print("\nFeatures after Standard Scaling:")
print(feat_standard_scaler)

# Feature Scaling - MinMaxScaler
mms = MinMaxScaler(feature_range=(0, 1))
feat_minmax_scaler = mms.fit_transform(final_set)

print("\nFeatures after MinMax Scaling:")
print(feat_minmax_scaler)