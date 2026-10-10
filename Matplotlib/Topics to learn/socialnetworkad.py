
# ==========================================
# SOCIAL NETWORK ADS - EXPLORATORY DATA ANALYSIS
# ==========================================

# 1. Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 2. Load the dataset
data = pd.read_csv(
    r"D:\New folder\Matplotlib\Topics to learn\Social_Network_Ads.csv"
)

# 3. Display basic information about the dataset
# Shows column names, data types, non-null values, and memory usage
data.info()

# 4. Display statistical summary
# Shows count, mean, standard deviation, minimum, quartiles, and maximum
print(data.describe())

# 5. Display the exact column names
# Check that the names used in the plots match your CSV
print(data.columns.tolist())

# 6. Select numerical columns
# Useful for correlation calculations
numeric_data = data.select_dtypes(include="number")

# 7. Correlation heatmap
# Shows correlations between numerical columns
plt.figure(figsize=(8, 6))
sns.heatmap(
    numeric_data.corr(),
    annot=True,
    linewidths=1,
    cmap="coolwarm"
)
plt.title("Social Network Ads - Correlation Heatmap")
plt.show()

# 8. Pairplot
# Shows pairwise relationships between numerical variables
# Colors represent whether the customer purchased
sns.pairplot(data, hue="Purchased", height=3)
plt.show()

# 9. Count customers by purchase status
# Prints the number of customers in each Purchased category
print(data["Purchased"].value_counts())

# 10. Countplot
# Compares the number of customers who purchased and did not purchase
sns.countplot(x="Purchased", data=data)
plt.title("Purchase Count")
plt.show()

# 11. One-hot encoding
# Converts Gender into numerical 0/1 columns
# Purchased remains unchanged as the target column
finalDataSet = pd.get_dummies(
    data,
    columns=["Gender"],
    dtype=int
)

# Display the first five rows of the encoded dataset
print(finalDataSet.head())

# 12. Scatterplot: Age vs Estimated Salary
# Colors distinguish customers by purchase status
sns.scatterplot(
    x="Age",
    y="EstimatedSalary",
    hue="Purchased",
    data=data
)
plt.title("Age vs Estimated Salary by Purchase Status")
plt.show()

# 13. Scatterplot: Age vs Purchased
# Purchased is binary (usually 0 or 1), so points appear in two bands
sns.scatterplot(
    x="Age",
    y="Purchased",
    data=data
)
plt.title("Age vs Purchase Status")
plt.show()

# 14. Scatterplot: Estimated Salary vs Purchased
# Helps explore how purchase status varies across salary values
sns.scatterplot(
    x="EstimatedSalary",
    y="Purchased",
    data=data
)
plt.title("Estimated Salary vs Purchase Status")
plt.show()

# 15. FacetGrid: Age vs Estimated Salary by purchase status
# Creates separate scatterplot panels for each Purchased category
g = sns.FacetGrid(data, col="Purchased", height=5)

g.map_dataframe(
    sns.scatterplot,
    x="Age",
    y="EstimatedSalary"
)

plt.show()

# 16. FacetGrid: Color points by Gender
# Separate panels represent purchase status
# Point colors represent Gender
g = sns.FacetGrid(
    data,
    col="Purchased",
    hue="Gender",
    height=5
)

g.map_dataframe(
    sns.scatterplot,
    x="Age",
    y="EstimatedSalary"
)

g.add_legend()
plt.show()

# 17. Boxplot: Age by purchase status
# Compares the age distribution of purchasers and non-purchasers
sns.boxplot(
    x="Purchased",
    y="Age",
    data=data
)
plt.title("Age Distribution by Purchase Status")
plt.show()

# 18. Boxplot: Estimated Salary by purchase status
# Compares salary distributions for the two purchase groups
sns.boxplot(
    x="Purchased",
    y="EstimatedSalary",
    data=data
)
plt.title("Estimated Salary by Purchase Status")
plt.show()

# 19. Boxplot: Overall age distribution
# Displays the median, quartiles, spread, and potential outliers
sns.boxplot(
    y="Age",
    data=data
)
plt.title("Overall Age Distribution")
plt.show()

# 20. Boxplot: Overall estimated salary distribution
sns.boxplot(
    y="EstimatedSalary",
    data=data
)
plt.title("Overall Estimated Salary Distribution")
plt.show()