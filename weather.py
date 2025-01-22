# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Replace 'path_to_weather_data.csv' with the actual path to your weather dataset
weather = pd.read_csv("path_to_weather_data.csv")

# Step 2: Preview the dataset
print("Dataset Information:")
print(weather.info())  # Check columns and data types
print("\nFirst 5 rows of the dataset:")
print(weather.head())  # Preview the data

# Step 3: Data Cleaning and Preparation
# Convert 'Date' column to datetime if it exists
if 'Date' in weather.columns:
    weather['Date'] = pd.to_datetime(weather['Date'])

# Extract month from 'Date' if 'Date' column exists
if 'Date' in weather.columns:
    weather['Month'] = weather['Date'].dt.month

# Check for required columns before proceeding
if 'Temperature' not in weather.columns or 'Humidity' not in weather.columns:
    raise ValueError("The dataset must contain 'Temperature' and 'Humidity' columns.")

# Step 4: Plot Monthly Temperature Trends
if 'Month' in weather.columns:
    # Calculate average temperature per month
    monthly_temp = weather.groupby('Month')['Temperature'].mean().reset_index()

    # Plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=monthly_temp, x='Month', y='Temperature', marker='o', color='blue')
    plt.title('Monthly Average Temperature Trends', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Average Temperature (°C)', fontsize=12)
    plt.xticks(range(1, 13), labels=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Step 5: Show the Relationship Between Humidity and Temperature
plt.figure(figsize=(10, 6))
sns.scatterplot(data=weather, x='Temperature', y='Humidity', alpha=0.7, color='green')
plt.title('Relationship Between Humidity and Temperature', fontsize=16)
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Humidity (%)', fontsize=12)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.show()
