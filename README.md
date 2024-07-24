# Rock vs. Mine Prediction

This project implements a machine learning model using Logistic Regression to classify objects as either "Rock" or "Mine" based on sonar data.

## Functionality

Leverages the scikit-learn library for data manipulation and model training.
Loads sonar data from a CSV file.
Preprocesses the data by handling missing values and converting non-numeric data.
Splits the data into training and testing sets for model evaluation.
Trains a Logistic Regression model on the training data.
Evaluates the model's accuracy on both training and testing data.
Provides a prediction system for classifying a new data point as "Rock" or "Mine."
## Dependencies

- numpy
- pandas
- scikit-learn
## Usage

Install dependencies:

   ```Bash
      pip install numpy pandas scikit-learn
   ```


Run the script:

   ```Bash
       python Rock_vs_Mine_Prediction.ipynb
   ```

This will execute the code in the Jupyter Notebook, performing data loading, training, evaluation, and prediction.

## Input Data Format

The prediction system expects a list of 60 floating-point numbers representing sonar readings for a single object. You can replace the provided input_data example with your own data.

## Output

The script will print the model's accuracy on the training and testing data, followed by the predicted class ("Rock" or "Mine") for the input data.

## Additional Notes

Ensure the data in your CSV file matches the format expected by the script (60 columns of numeric values, with the last column representing the class label).

## Contributing

Feel free to submit pull requests with improvements or additional functionalities.
