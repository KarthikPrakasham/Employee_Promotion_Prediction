import streamlit as st
import pandas as pd
import joblib

st.title("Employee Performance Prediction App")
dataFrame = pd.read_csv("train.csv")

employee_id = st.number_input("Enter Employee ID:", min_value=0, step=1)
department = st.selectbox("Select Department:", dataFrame['department'].unique())
region = st.selectbox("Select Region:", dataFrame['region'].unique())
education = st.selectbox("Select Education Level:", dataFrame['education'].unique())
gender = st.selectbox("Select Gender:", dataFrame['gender'].unique())
recruitment_channel = st.selectbox("Select Recruitment Channel:", dataFrame['recruitment_channel'].unique())
no_of_trainings = st.number_input("Enter Number of Trainings:", min_value=0, step=1)
age = st.number_input("Enter Age:", min_value=18, step=1)
previous_year_rating = st.number_input("Enter Previous Year Rating (1-5):", min_value=1, max_value=5, step=1)
length_of_service = st.number_input("Enter Length of Service (in years):", min_value=0, step=1)
KPIs_met_80_percent = st.number_input("Enter KPIs Met >80% (0 or 1):", min_value=0, max_value=1, step=1)
awards_won = st.number_input("Enter Awards Won (0 or 1):", min_value=0, max_value=1, step=1)
avg_training_score = st.number_input("Enter Average Training Score (0-100):", min_value=0, max_value=100, step=1)

input_data = pd.DataFrame({
    'employee_id': [employee_id],
    'department': [department],
    'region': [region],
    'education': [education],
    'gender': [gender],
    'recruitment_channel': [recruitment_channel],
    'no_of_trainings': [no_of_trainings],
    'age': [age],
    'previous_year_rating': [previous_year_rating],
    'length_of_service': [length_of_service],
    'KPIs_met >80%': [KPIs_met_80_percent],
    'awards_won?': [awards_won],
    'avg_training_score': [avg_training_score]
})

if st.button("Predict Promotion"):
    model = joblib.load("../employee_promotion_model.pkl")
    input_data['education_score'] = input_data['education'].replace({'Bachelor\'s':1,'Master\'s & above':2,'Below Secondary':0})
    input_data['recruitment_channel_score'] = input_data['recruitment_channel'].replace({'sourcing':1,'other':0,'referred':2})
    input_data['department_score'] = input_data['department'].replace({'Sales & Marketing':1,'Operations':2,'Procurement':3,'Technology':4,'Analytics':5,'R&D':6,'Finance':7,'HR':8,'Legal':9})
    input_data['gender_score'] = input_data['gender'].replace({'m':1,'f':0})
    input_data['high_performer'] = input_data['KPIs_met >80%'] * input_data['awards_won?']
    prediction = model.predict(input_data.drop(columns=['employee_id']))
    if prediction[0] == 1:
        st.success("The employee is likely to be promoted.")
    else:
        st.info("The employee is not likely to be promoted.")