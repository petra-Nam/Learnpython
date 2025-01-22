# Importing required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Replace 'path_to_dataset' with the path where you saved the MovieLens dataset
ratings = pd.read_csv("/Users/I750363/Downloads/Sample - Superstore 5.csv")

# Step 2: Preview the dataset
print("First 5 rows of the dataset:")
print(ratings.head())

# Step 3: Plot the distribution of movie ratings
plt.figure(figsize=(8, 6))  # Set the figure size
sns.histplot(data=ratings, x='rating', bins=10, kde=True, color='blue')  # Create the histogram
plt.title('Distribution of Movie Ratings', fontsize=16)  # Title of the plot
plt.xlabel('Rating', fontsize=12)  # X-axis label
plt.ylabel('Count', fontsize=12)  # Y-axis label
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Optional: Add grid lines for better readability
plt.show()
