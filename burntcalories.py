import numpy as np
from joblib import load

model=load('Calories_Burnt.joblib')

def predict_burnt_calories(Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp):
    features=np.array([[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]])
    calories_burnt=model.predict(features)
    return calories_burnt[0]