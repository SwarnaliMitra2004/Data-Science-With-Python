import pandas as pd

from pathlib import Path

# Find cars.csv in the same folder as this Python script
file_path = Path(__file__).parent / "50_Startups.csv"
startups = pd.read_csv(file_path)

# Statistical summary
print("Statistical Summary:")
print(startups.describe())

# Correlation coefficient
print("\nCorrelation Matrix:")
print(startups.corr(numeric_only=True))