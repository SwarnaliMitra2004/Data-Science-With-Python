
# 1. Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 2. Load the salary dataset
data = pd.read_csv(
    r"D:\New folder\Matplotlib\Topics to learn\Salary_Data.csv"
)

# 3. Display dataset information
# Shows column names, data types, non-null values, and memory usage
data.info()

# 4. Display statistical summary
# Shows count, mean, standard deviation, quartiles, etc.
print(data.describe())

# 5. Select numerical columns
# Useful for correlation and numerical analysis
numeric_data = data.select_dtypes(include="number")

# 6. Correlation heatmap
# Shows the strength and direction of relationships between numerical columns
plt.figure(figsize=(8, 6))
sns.heatmap(
    numeric_data.corr(),
    annot=True,
    linewidths=1,
    cmap="coolwarm"
)
plt.title("Salary Dataset - Correlation Heatmap")
plt.show()

# 7. Pairplot
# Shows relationships between pairs of numerical variables
sns.pairplot(data, height=3)
plt.show()

# 8. Scatterplot: Years of Experience vs Salary
# Helps explore how salary changes with work experience
sns.scatterplot(
    x="YearsExperience",
    y="Salary",
    data=data
)
plt.title("Years of Experience vs Salary")
plt.show()

# 9. Regression plot
# Shows the relationship between experience and salary
# The line represents a fitted linear trend
sns.regplot(
    x="YearsExperience",
    y="Salary",
    data=data
)
plt.title("Experience vs Salary - Regression Plot")
plt.show()

# 10. Boxplot: Years of Experience
# Displays the distribution and potential outliers
sns.boxplot(
    y="YearsExperience",
    data=data
)
plt.title("Years of Experience Distribution")
plt.show()

# 11. Boxplot: Salary
# Displays salary distribution and potential outliers
sns.boxplot(
    y="Salary",
    data=data
)
plt.title("Salary Distribution")
plt.show()