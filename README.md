**Employee Promotion Prediction**

📌 **Project Overview**

Employee promotions are critical for organizational growth, talent retention, and workforce planning.
This project builds a machine learning classification model to predict whether an employee is likely to be promoted based on historical HR data such as performance, experience, training, and demographics.
The goal is to help HR teams make data-driven promotion decisions while identifying key factors influencing promotions.

**FASTAPI** - https://employee-promotion-prediction-fastapi-860043820196.asia-south1.run.app/docs#/

**STREAMLIT** - https://employee-promotion-prediction-streamlit-860043820196.asia-south1.run.app/

🎯 **Problem Statement**

Given employee-level data, predict whether an employee will be promoted (1) or not (0).
This is a binary classification problem with class imbalance, making feature selection, model choice, and evaluation especially important.

🧠 **Key Concepts Used**

Exploratory Data Analysis (EDA)

Missing value handling

Feature engineering

Feature selection using tree-based models

Class imbalance handling

Model evaluation & tuning

End-to-end ML pipeline

🔍 **Feature Selection Strategy**

Tree-based feature importance methods were used:

Decision Trees – simple and interpretable

Random Forest – more stable and robust

XGBoost – final model with tuned hyperparameters

Only the most impactful features were retained to reduce overfitting and improve generalization.

🤖 **Model Used**

XGBoost Classifier

Handles non-linearity well

Works effectively with imbalanced data

Provides strong predictive performance

Hyperparameter tuning was performed to balance training accuracy and generalization performance.


👤 Author

Karthik Prakasham
📍 India
🔗 GitHub: https://github.com/KarthikPrakasham
