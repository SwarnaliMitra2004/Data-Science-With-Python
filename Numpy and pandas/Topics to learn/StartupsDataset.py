import pandas as pd

# Read the dataset
startups = pd.read_csv("50_startups.csv")

# Statistical summary
print("Statistical Summary:")
print(startups.describe())

# Correlation coefficient
print("\nCorrelation Matrix:")
print(startups.corr(numeric_only=True))