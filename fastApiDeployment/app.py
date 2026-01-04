from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

class EmployeeData(BaseModel):
    employee_id: int
    department: str
    region: str
    education: str
    gender: str
    recruitment_channel: str
    no_of_trainings: int
    age: int
    previous_year_rating: int
    length_of_service: int
    KPIs_met_80_percent: int
    awards_won: int
    avg_training_score: int

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
    input_data['high_performer'] = input_data['KPIs_met >80%'] * input_data['awards_won?']
    input_data['experience_level'] = pd.cut(input_data['length_of_service'], bins=[-1,2,5,10,50], labels=[0,1,2,3])
    model = joblib.load("../employee_promotion_model.pkl")
    prediction = model.predict(input_data.drop(columns=['employee_id']))
    if prediction[0] == 1:
        return {"message": "The employee is likely to be promoted."}
    else:
        return {"message": "The employee is not likely to be promoted."}