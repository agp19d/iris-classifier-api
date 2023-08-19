// index.js

// Import required modules
const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

// Define endpoint to predict iris species
app.get('/endpoint', (req, res) => {
    // Log the reception of a new request
    console.log('Received request. Parsing and validating features...');

    // Parse and validate features from query parameters
    let feature1 = parseFloat(req.query.feature1);
    let feature2 = parseFloat(req.query.feature2);
    let feature3 = parseFloat(req.query.feature3);
    let feature4 = parseFloat(req.query.feature4);

    // Check if any feature is NaN and respond with an error
    if (isNaN(feature1) || isNaN(feature2) || isNaN(feature3) || isNaN(feature4)) {
        return res.status(400).send('Invalid input features.');
    }

    // Define paths to Python executable and prediction script
    const pythonPath = './myenv/Scripts/python.exe';
    const scriptPath = './python_scripts/predict_iris.py';

    // Log start of Python script execution
    console.log('About to run the Python script...');

    // Spawn the Python process to execute the prediction script
    const pythonProcess = spawn(pythonPath, [scriptPath, feature1, feature2, feature3, feature4]);

    let result = '';
    let error = '';

    // Listen for data output from the Python script
    pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
    });

    // Listen for error messages from the Python script
    pythonProcess.stderr.on('data', (data) => {
        error += data.toString();
    });

    // Handle Python script completion or failure
    pythonProcess.on('close', (code) => {
        if (code !== 0) {
            console.error('Python script failed with code:', code);
            console.error('Error:', error);
            return res.status(500).send('Prediction failed.');
        } else {
            console.log('Python script executed. Result:', result);
            return res.send(result.trim());
        }
    });
});

// Start the Express server on the defined port
app.listen(port, () => {
    console.log(`Running on port ${port}!`);
});
