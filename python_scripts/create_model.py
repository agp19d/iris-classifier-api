# create_model.py

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Evaluate the classifier's accuracy on the test set
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.4f}")

# Save the model to a .pkl file
dump(clf, './python_scripts/iris_model.pkl')
