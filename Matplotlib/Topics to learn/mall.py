# 1. Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 2. Load the dataset
data = pd.read_csv(
    r"D:\New folder\Matplotlib\Topics to learn\Mall_Customers.csv"
)

# 3. Display basic information about the dataset
# Shows column names, data types, non-null values, and memory usage
data.info()

# 4. Display statistical summary
# Shows count, mean, standard deviation, minimum, maximum, and quartiles
print(data.describe())

# 5. Select only numerical columns
# Useful for numerical analysis and correlation calculations
numeric_data = data.select_dtypes(include="number")

# 6. Correlation heatmap
# Shows correlations between numerical columns
plt.figure(figsize=(10, 8))
sns.heatmap(
    numeric_data.corr(),
    annot=True,          # Display correlation values
    linewidths=2,        # Add space between cells
    cmap="coolwarm"      # Set the color palette
)
plt.title("Correlation Heatmap")
plt.show()

# 7. Pairplot
# Shows pairwise relationships between numerical variables
# Points are colored according to Gender
sns.pairplot(data, hue="Gender", height=3)
plt.show()

# 8. Count customers by Gender
# Prints the number of customers in each gender category
print(data.value_counts("Gender"))

# 9. Countplot
# Displays the number of customers in each gender category
sns.countplot(x="Gender", data=data)
plt.title("Customer Count by Gender")
plt.show()

# 10. One-hot encoding
# Converts the categorical Gender column into numerical 0/1 columns
# The original Gender column is replaced by the encoded columns
finalDataSet = pd.get_dummies(
    data,
    columns=["Gender"],
    dtype=int
)

# Display the first five rows of the encoded dataset
print(finalDataSet.head())

# 11. Scatterplot: Age vs Annual Income
# Each point represents a customer
# Colors distinguish customers by Gender
sns.scatterplot(
    x="Age",
    y="Annual Income (k$)",
    hue="Gender",
    data=data
)
plt.title("Age vs Annual Income")
plt.show()

# 12. Scatterplot: Annual Income vs Spending Score
# Helps explore the relationship between income and spending score
sns.scatterplot(
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Gender",
    data=data
)
plt.title("Annual Income vs Spending Score")
plt.show()

# 13. Scatterplot: Age vs Spending Score
# Helps explore how spending scores vary with customer age
sns.scatterplot(
    x="Age",
    y="Spending Score (1-100)",
    hue="Gender",
    data=data
)
plt.title("Age vs Spending Score")
plt.show()

# 14. FacetGrid: Age vs Spending Score by Gender
# Creates a separate scatterplot panel for each gender
g = sns.FacetGrid(data, col="Gender")

g.map_dataframe(
    sns.scatterplot,
    x="Age",
    y="Spending Score (1-100)"
)

plt.show()

# 15. FacetGrid: Annual Income vs Spending Score by Gender
# Allows comparison of income and spending patterns between genders
g = sns.FacetGrid(data, col="Gender", height=5)

g.map_dataframe(
    sns.histplot,
    x="Annual Income (k$)",
    y="Spending Score (1-100)"
)

plt.show()

# 16. FacetGrid: Color points according to Age
# Separate panels represent Gender; point colors represent Age
g = sns.FacetGrid(
    data,
    col="Gender",
    hue="Age",
    height=5
)

g.map_dataframe(
    sns.scatterplot,
    x="Annual Income (k$)",
    y="Spending Score (1-100)"
)

g.add_legend()  # Display the Age color legend
plt.show()

# 17. Boxplot: Spending Score by Gender
# Compares the distribution of spending scores between genders
sns.boxplot(
    x="Gender",
    y="Spending Score (1-100)",
    data=data
)
plt.title("Spending Score by Gender")
plt.show()

# 18. Boxplot: Annual Income by Gender
# Compares the distribution of annual income between genders
sns.boxplot(
    x="Gender",
    y="Annual Income (k$)",
    data=data
)
plt.title("Annual Income by Gender")
plt.show()

# 19. Boxplot: Overall Age distribution
# Shows the median, quartiles, spread, and potential outliers in Age
sns.boxplot(
    y="Age",
    data=data
)
plt.title("Age Distribution")
plt.show()
