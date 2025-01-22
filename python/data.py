import pandas as pd

# Load the Superstore dataset (adjust the file path if needed)
df = pd.read_csv("https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv")

# Check the columns and the first few rows of the dataset
print(df.columns)  # To check column names
print(df.head())   # To display the first few rows

# Fill missing sales data with 0 (or other strategy like mean or median)
df['Sales'] = df['Sales'].fillna(0)

# Check for any missing values
print(df.isnull().sum())  # This will print the count of missing values for each column

# Group by Region and Product Category to get the sum of Sales
sales_by_region_category = df.groupby(['Region', 'Category'])['Sales'].sum().reset_index()

# Display the grouped sales data
print(sales_by_region_category)

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Year and Month from the 'Order Date' to create 'YearMonth' column
df['YearMonth'] = df['Order Date'].dt.to_period('M')

# Create the pivot table to show sales by Year-Month, Region, and Category
pivot_table = pd.pivot_table(df, values='Sales', index=['YearMonth'], columns=['Region', 'Category'], aggfunc='sum', fill_value=0)

# Display the pivot table
print(pivot_table)

# Fill missing values in the pivot table with 0 (although you already did this above)
pivot_table = pivot_table.fillna(0)

# Display the final pivot table
print(pivot_table)

