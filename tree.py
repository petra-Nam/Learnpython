import numpy as np  # numpy for numerical computations and handling arrays
import pandas as pd  # pandas for data manipulation and analysis
from sklearn.model_selection import train_test_split  # sklearn for machine learning, train_test_split for splitting data into training and testing sets
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree  # DecisionTreeClassifier for creating a decision tree model, export_text for textual representation, plot_tree for graphical visualization
from sklearn.metrics import accuracy_score, classification_report  # accuracy_score for evaluating the accuracy of the model, classification_report for detailed performance metrics
from sklearn.datasets import load_iris  # load_iris for loading the Iris dataset
import matplotlib.pyplot as plt  # matplotlib for plotting

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame from the dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target

# Display the first few rows of the DataFrame
print(iris_df.head())

# Define features (X) and target (y)
X = iris_df.drop(columns='target')
y = iris_df['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the training and testing sets
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

# Initialize the Decision Tree Classifier
# We’re using a pre-built model from sklearn. Here, criterion decides how splits are chosen (Gini Impurity or Entropy), and max_depth controls how deep the tree can grow.
# The max_depth parameter controls the maximum number of levels (splits) in the decision tree.
clf = DecisionTreeClassifier(criterion='gini', max_depth=3)

# Train the model using the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# Evaluate the model using additional metrics
# Accuracy measures the proportion of correct predictions. Precision, recall, and F1-score provide a deeper understanding of performance.
report = classification_report(y_test, y_pred, target_names=iris.target_names)
print(report)

# Visualize the tree rules
# This text output shows how the model splits the data. Each rule is based on a threshold for a feature.
tree_rules = export_text(clf, feature_names=list(X.columns))
print(tree_rules)

# Graphical visualization of the decision tree
# This plot helps us understand the decision-making process visually.
plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()