# -----------------------------------------
# Exploratory Data Analysis on Retail Sales
# Oasis Infobyte Internship Project
# Author: Chiranthan S
# -----------------------------------------

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the retail sales dataset
sales_data = pd.read_csv("retail_sales_dataset.csv")

print("Dataset successfully loaded!\n")

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(sales_data.head())

print("\n----------------------------------")

# Display basic information about dataset
print("Dataset Information:")
print(sales_data.info())

print("\n----------------------------------")

# Display statistical summary
print("Statistical Summary:")
print(sales_data.describe())

print("\n----------------------------------")

# Check if dataset contains missing values
print("Checking for missing values:")
print(sales_data.isnull().sum())

print("\n----------------------------------")

# Total number of records
print("Total number of transactions:", len(sales_data))

# -----------------------------
# DATA VISUALIZATION
# -----------------------------

# Visualization 1: Product category sales count
plt.figure()
sns.countplot(data=sales_data, x="Product Category")
plt.title("Number of Sales in Each Product Category")
plt.xlabel("Product Category")
plt.ylabel("Number of Transactions")
plt.show()

# Visualization 2: Distribution of purchase amounts
plt.figure()
plt.hist(sales_data["Total Amount"], bins=15)
plt.title("Distribution of Purchase Amounts")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.show()

# Visualization 3: Gender-based purchase analysis
plt.figure()
sns.countplot(data=sales_data, x="Gender")
plt.title("Number of Purchases by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Visualization 4: Relationship between age and spending
plt.figure()
plt.scatter(sales_data["Age"], sales_data["Total Amount"])
plt.title("Customer Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.show()

# -----------------------------
# BASIC SALES INSIGHTS
# -----------------------------

total_sales = sales_data["Total Amount"].sum()
average_sale = sales_data["Total Amount"].mean()
highest_sale = sales_data["Total Amount"].max()

print("\nSales Insights:")
print("Total Revenue:", total_sales)
print("Average Purchase Amount:", average_sale)
print("Highest Purchase Amount:", highest_sale)

# Save processed dataset
sales_data.to_csv("retail_sales_processed.csv", index=False)

print("\nProcessed dataset saved successfully!")