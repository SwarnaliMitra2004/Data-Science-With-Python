import pandas as pd
from pathlib import Path

# Find cars.csv in the same folder as this Python script
file_path = Path(__file__).parent / "cars.csv"
cars = pd.read_csv(file_path)

# Inspect the first 10 rows
print("First 10 rows:")
print(cars.head(10))

# Print the complete DataFrame
print("\nComplete DataFrame:")
print(cars)

# Inspect the last 5 rows
print("\nLast 5 rows:")
print(cars.tail(5))

# Get meta information
print("\nDataFrame Information:")
print(cars.info())