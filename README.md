**Employee Promotion Prediction**

📌 Project Overview

Employee promotions are critical for organizational growth, talent retention, and workforce planning.
This project builds a machine learning classification model to predict whether an employee is likely to be promoted based on historical HR data such as performance, experience, training, and demographics.
The goal is to help HR teams make data-driven promotion decisions while identifying key factors influencing promotions.

🎯 Problem Statement

Given employee-level data, predict whether an employee will be promoted (1) or not (0).
This is a binary classification problem with class imbalance, making feature selection, model choice, and evaluation especially important.

Employee_Promotion_Prediction/
│
├── fastApiDeployment/
│   ├── app.py
│   └── DockerFile
│   └── employee_promotion_model.pkl
│   └── requirements.txt
│
├── resources/
│   ├── sample_submission.csv
│   ├── submission_Logistic.csv
│   └── submission_XGB.csv
│   └── submission_XGB_Final.csv
│   └── train.csv
│   └── test.csv
│
├── streamLitApiDeployment/
│   ├── app.py
│   └── DockerFile
│   └── employee_promotion_model.pkl
│   └── requirements.txt
│   └── train.csv
│
├── src/
│   ├── preprocessing.py
│   ├── feature_selection.py
│   └── model_pipeline.py
│
├── employee_promotion_model.pkl
└── myNoteBook.ipynb
└── README.md
