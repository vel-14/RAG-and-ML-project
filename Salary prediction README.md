# Employee Salaries Analysis and Regression Model

## Overview

This project analyzes a dataset of employee salaries and builds several regression models to predict base salary. The analysis includes data cleaning, visualization, and model evaluation. The primary goal is to understand the factors affecting employee salaries and to accurately predict future salaries using different machine learning algorithms.

## Dataset

The dataset used in this project is `Employee_Salaries.csv`, which contains information about employee salaries, departments, and other related attributes.

## Libraries Used

- pandas
- numpy
- seaborn
- matplotlib
- sklearn

## Data Cleaning

1. **Handling Missing Values**:
   - Checked for null values since the null value is less than 1%,  dropped any rows containing null values.

2. **Handling Duplicates**:
   - Identified and dropped duplicate rows. Initial analysis showed more than 5% duplicates which were further investigated and removed to avoid skewing the data.

## Data Visualization

1. **Distribution and Outliers**:
   - Used box plots and histograms to visualize the distribution and identify outliers for numeric columns such as `Base_Salary`, `Overtime_Pay`, and `Longevity_Pay`.

2. **Department Analysis**:
   - Plotted the average salary per department and identified top departments by average salary.

3. **Department Occurrences**:
   - Visualized the count of occurrences for the top 10 departments.

4. **Gender Distribution and Pay Gap**:
   - Analyzed the gender distribution and the average base salary by gender.

5. **Grade Analysis**:
   - Visualized the average base salary by grade, showing how salary varies based on grade.

6. **Correlation Analysis**:
   - Used a heatmap to visualize the correlation between different features.

## Data Preprocessing

1. **Encoding Categorical Variables**:
   - Used `OrdinalEncoder` for hierarchical features like `Department` and `Grade`.
   - Used `LabelEncoder` for other categorical features like `Gender` and `Division`.

## Regression Models

The following regression models were built and evaluated:

1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**
4. **Gradient Boosting Regressor**

## Model Evaluation

The models were evaluated based on the following metrics:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R-squared (R2) Score

### Insights

- **Decision Tree Regressor** showed a higher R2 score for training data, but the R2 score for test data was lower than the Random Forest Regressor.
- **Random Forest Regressor** provided a good R2 score for both training and test data, indicating better generalization compared to the Decision Tree Regressor.


## Conclusion

This analysis provides valuable insights into the factors affecting employee salaries and demonstrates the effectiveness of using ensemble methods like Random Forest for regression tasks. Future work can include exploring additional features and refining the models for even better predictions.

## How to Run

1. Ensure you have all the required libraries installed.
2. Place the `Employee_Salaries.csv` file in the specified path.
3. Run the provided code to perform the analysis and build the regression models.

