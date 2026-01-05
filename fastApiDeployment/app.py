from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI()

class EmployeeData(BaseModel):
    employee_id: int | None = 123456
    department: str | None = 'Operations'
    region: str | None = 'region_22'
    education: str | None = 'Master\'s & above'
    gender: str | None = 'm'
    recruitment_channel: str | None = 'sourcing'
    no_of_trainings: int | None = 2
    age: int | None = 27
    previous_year_rating: int | None = 4
    length_of_service: int | None = 13
    KPIs_met_80_percent: int | None = 1
    awards_won: int | None = 1
    avg_training_score: int | None = 95

@app.get("/")
def read_root():
    return {"Welcome": "to the Employee Promotion Prediction API"}

@app.post("/predict_promotion/")
def predict_promotion(data: EmployeeData):
    input_data = pd.DataFrame([data.dict()])
    input_data['education_score'] = input_data['education'].replace({'Bachelor\'s':1,'Master\'s & above':2,'Below Secondary':0})
    input_data['recruitment_channel_score'] = input_data['recruitment_channel'].replace({'sourcing':1,'other':0,'referred':2})
    input_data['department_score'] = input_data['department'].replace({'Sales & Marketing':1,'Operations':2,'Procurement':3,'Technology':4,'Analytics':5,'R&D':6,'Finance':7,'HR':8,'Legal':9})
    input_data['gender_score'] = input_data['gender'].replace({'m':1,'f':0})
    input_data['high_performer'] = input_data['KPIs_met_80_percent'] * input_data['awards_won']
    input_data['is_new_joiner'] = np.where(input_data['previous_year_rating'] == 0, 1, 0)
    input_data['KPIs_met >80%'] = input_data['KPIs_met_80_percent']
    input_data['awards_won?'] = input_data['awards_won']
    model = joblib.load("employee_promotion_model.pkl")
    prediction = model.predict(input_data.drop(columns=['employee_id']))
    if prediction[0] == 1:
        return {"message": "The employee is likely to be promoted."}
    else:
        return {"message": "The employee is not likely to be promoted."}