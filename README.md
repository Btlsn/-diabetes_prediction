# Diabetes Prediction with Machine Learning

This project is a machine learning application designed to predict diabetes status based on a variety of health and lifestyle factors. The project uses a synthetic dataset and evaluates multiple machine learning algorithms to determine the best-performing model. The selected model is then saved for future use.

## Dataset Description
The dataset consists of 13 features and a target variable (`Diabetes_Status`) indicating whether the individual has diabetes (1) or not (0). The features are:

- **Age**: Age of the individual (18-80 years)
- **Gender**: Gender of the individual (Male, Female)
- **BMI**: Body Mass Index (15-50)
- **Blood_Sugar_Level**: Blood sugar level (70-200 mg/dL)
- **Family_History**: Whether there is a family history of diabetes (Yes, No)
- **Blood_Pressure**: Blood pressure (90-180 mmHg)
- **Cholesterol_Level**: Cholesterol level (150-350 mg/dL)
- **Smoking**: Smoking habit (Yes, No)
- **Alcohol_Consumption**: Alcohol consumption habit (Yes, No)
- **Sleep_Duration**: Sleep duration in hours (4-10 hours)
- **Exercise_Frequency**: Days of exercise per week (0-7 days)

## Project Workflow

1. **Data Generation**:
   - Synthetic data was generated using Python’s `random` library to simulate realistic health and lifestyle data.
   - The generated data was saved as a CSV file for use in the project.

2. **Data Preprocessing**:
   - The dataset was loaded into a pandas DataFrame.
   - Categorical features (e.g., Gender, Smoking) were encoded using one-hot encoding.
   - The dataset was split into training (80%) and testing (20%) sets.

3. **Model Training and Evaluation**:
   - Ten different machine learning algorithms were evaluated:
     - Logistic Regression
     - Random Forest
     - Decision Tree
     - K-Nearest Neighbors
     - Support Vector Machine
     - Naive Bayes
     - Gradient Boosting
     - AdaBoost
     - Bagging Classifier
     - Extra Trees
   - Models were evaluated using accuracy as the performance metric.

4. **Best Model Selection**:
   - The best-performing model was identified based on accuracy.
   - The selected model was saved in `joblib` format for future use.

5. **Results**:
   - All models' performance metrics were saved to a CSV file.
   - The best model’s accuracy and details were logged and displayed.

## Files in the Repository

- **algoritma.ipynb**: Jupyter Notebook containing the full implementation of the project, from data generation to model evaluation.
- **veri.csv**: The synthetic dataset used for training and testing.
- **model_scores.csv**: A CSV file summarizing the accuracy of all evaluated models.
- **eniyi.joblib**: The saved best-performing machine learning model.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook algoritma.ipynb
   ```

4. Run all cells to see the implementation and results.

5. To use the saved model for predictions, load `eniyi.joblib` and input new data points.

## Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn
- joblib
- Jupyter Notebook

## Future Improvements

- Incorporate real-world datasets to enhance the model's reliability.
- Explore additional machine learning algorithms and hyperparameter tuning.
- Develop a user-friendly interface for predictions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to the project or report issues! Your feedback is highly appreciated.

