# Iris Classifier Service
This project integrates a Python-based Iris classifier with an Express.js server. Users can make HTTP requests to predict the Iris class based on four provided features.

## Structure
python_scripts/: Contains Python scripts for training and predicting.
server/: Holds the Express.js application for serving predictions.

## Setup
Prerequisites
Python (Recommend 3.7 or later)
Node.js (Recommend 14.x or later)

## Steps
1. Clone the repository:

``` bash
git clone [YOUR_GITHUB_REPO_LINK]
cd iris_classifier_service
```

2. Set up Python environment:

``` bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# For Windows
myenv\Scripts\activate

# For macOS and Linux
source myenv/bin/activate

# Install required packages
pip install -r requirements.txt
```

3. Set up Node.js environment:

``` bash
cd server
npm install
```

## Running the Services
Train the model (only need to do this once):

``` bash
python python_scripts/create_model.py
```

Start the Express.js server:

``` bash
cd server
node index.js
```

The server should now be running on port 3000. You can make requests to http://localhost:3000/endpoint with the required query parameters (feature1, feature2, feature3, and feature4) to get predictions.

## Usage
To get a prediction, send a GET request with the desired Iris features:

``` bash
curl http://localhost:3000/endpoint?feature1=<VALUE>&feature2=<VALUE>&feature3=<VALUE>&feature4=<VALUE>
```

Replace <VALUE> with your feature values. The response will contain the predicted Iris class.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

