# Number Prediction using Linear Regression (Python)

## Project Overview

This project demonstrates how to build a simple Number Prediction system using **Linear Regression** in Python.

The model predicts exam scores based on the number of hours studied.

It is a beginner-friendly Machine Learning project that explains:
- Supervised Learning
- Regression
- Model Training
- Prediction
- Data Visualization


## What is Linear Regression?

Linear Regression is a supervised machine learning algorithm used to predict continuous values.

It follows the equation:

    y = mx + b

Where:
- m = slope
- b = intercept
- x = input feature
- y = predicted output

The model finds the best-fit line that minimizes prediction error.


## 🛠 Technologies Used

- Python 3.x
- NumPy
- Matplotlib
- Scikit-learn



## 📂 Project Structure

```
number_prediction/
│
├── main.py
├── requirements.txt
├── venv/
└── README.md

```

## 📊 Dataset Used

| Hours Studied | Exam Score |
|--------------|------------|
| 1            | 45         |
| 2            | 50         |
| 3            | 60         |
| 4            | 70         |
| 5            | 80         |

The model is trained on this dataset and predicts score for 6 hours of study.

### Install dependencies

    pip install -r requirements.txt

### Run the project

    python main.py



## Output

- Predicted exam score printed in terminal
- Regression graph showing:
  - Blue dots → Actual data
  - Line → Predicted regression line


## Learning Outcomes

After completing this project, I understood:

- How Linear Regression works
- How machine learning models are trained
- How prediction works mathematically
- How to use Scikit-learn for regression
- How to visualize results using Matplotlib
- How to manage Python environments using venv

