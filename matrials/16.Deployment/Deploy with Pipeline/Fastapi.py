from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

with open("Pipeline.pkl", "rb") as f:
    model = pickle.load(f)

feature_order = ['Time_spent_Alone',	'Stage_fear',	'Social_event_attendance',	'Going_outside',	'Drained_after_socializing',	'Friends_circle_size',	'Post_frequency']

app = FastAPI()

class InputData(BaseModel):
    Time_spent_Alone: float
    Stage_fear: str
    Social_event_attendance: float
    Going_outside: float
    Drained_after_socializing: str
    Friends_circle_size: float
    Post_frequency: float

@app.post("/predict")
def predict(data: InputData):
    input_dict = data.dict()
    df = pd.DataFrame([input_dict], columns=feature_order)
    df['Stage_fear'] = df['Stage_fear'].str.lower().str.capitalize()
    df['Drained_after_socializing'] = df['Drained_after_socializing'].str.lower().str.capitalize()

    prediction = model.predict(df)[0]

    if(prediction == 1):
        return {'result': 'You are an Extrovert!'}
    else:
        return {'result': 'You are an Introvert!'}
