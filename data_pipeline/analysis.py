import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('products.csv')

# Check for missing values
print(df.isnull().sum())

# Fill or drop missing values if any
df.dropna(inplace=True)  # Drop rows with missing values
# or
# df.fillna(method='ffill', inplace=True)  # Fill missing values

# Ensure 'Price' is numeric (remove currency symbols and convert)
df['Price'] = df['Price'].replace({'₹': '', ',': ''}, regex=True).astype(float)


# Summary statistics
print(df.describe())

# Frequency of products
print(df['Product Name'].value_counts())

# Average price
print(f"Average Price: {df['Price'].mean()}")

# Price range
print(f"Price Range: {df['Price'].min()} - {df['Price'].max()}")



plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=20, kde=True)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()
top_expensive = df.nlargest(10, 'Price')

plt.figure(figsize=(12, 8))
sns.barplot(x='Price', y='Product Name', data=top_expensive, palette='viridis',hue="Product Name",legend=False)
plt.title('Top 10 Most Expensive Products')
plt.xlabel('Price')
plt.ylabel('Product Name')
plt.show()

plt.figure(figsize=(14, 8))
sns.scatterplot(x='Product Name', y='Price', data=df)
plt.xticks(rotation=90)
plt.title('Price vs. Product Name')
plt.xlabel('Product Name')
plt.ylabel('Price')
plt.show()
