# predict_iris.py

# Import necessary libraries and modules
import sys
from joblib import load
import numpy as np

def main():
    # Ensure that the user provides exactly 4 features
    if len(sys.argv) != 5:
        print("You must provide exactly 4 features for prediction.")
        return

    # Convert command-line arguments to floating-point numbers
    input_features = list(map(float, sys.argv[1:]))

    # Check for invalid input features (NaN or infinity)
    if any(np.isnan(input_features)) or any(np.isinf(input_features)):
        print("Invalid input features detected.")
        return
    
    # Load the trained machine learning model
    model = load('./python_scripts/iris_model.pkl')

    # Make a prediction using the provided features
    prediction = model.predict([input_features])

    # Define the names of the iris classes
    iris_classes = ["setosa", "versicolor", "virginica"]

    # Output the predicted class
    print(f"Predicted class index: {prediction[0]} ({iris_classes[prediction[0]]})")

# Ensure the script is being run as the main module
if __name__ == "__main__":
    main()
