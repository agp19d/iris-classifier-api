# predict_iris.py
import sys
from joblib import load
import numpy as np
import os

def main():
    if len(sys.argv) != 5:
        print("You must provide exactly 4 features for prediction.")
        return

    input_features = list(map(float, sys.argv[1:]))

    if any(np.isnan(input_features)) or any(np.isinf(input_features)):
        print("Invalid input features detected.")
        return
    
    print(os.getcwd())
    model = load('./python_scripts/iris_model.pkl')
    prediction = model.predict([input_features])

    iris_classes = ["setosa", "versicolor", "virginica"]
    print(f"Predicted class index: {prediction[0]} ({iris_classes[prediction[0]]})")

if __name__ == "__main__":
    main()
