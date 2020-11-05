import pandas as pd
import uvicorn
import sklearn
import joblib
from fastapi import FastAPI

app = FastAPI()
modelLogisticRegression = joblib.load("modelLogisticRegression.pkl")
modelRandomForest = joblib.load("modelRandomForest.pkl")

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Using Get
@app.get('/predictRandomForest/{age}/{anaemia}/{creatinine_phosphokinase}/{diabetes}/{ejection_fraction}/{high_blood_pressure}/{platelets}/{serum_creatinine}/{serum_sodium}/{sex}/{smoking}')
async def predictRandomForest(age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking):
    heart_failure = pd.DataFrame({
    'age': [float(age)],
    'anaemia': [float(anaemia)],
    'creatinine_phosphokinase': [float(creatinine_phosphokinase)],
    'diabetes': [float(diabetes)],
    'ejection_fraction': [float(ejection_fraction)],
    'high_blood_pressure': [float(high_blood_pressure)],
    'platelets': [float(platelets)],
    'serum_creatinine': [float(serum_creatinine)],
    'serum_sodium': [float(serum_sodium)],
    'sex': [float(sex)],
    'smoking': [float(smoking)]
    })
    Y_pred = modelRandomForest.predict(heart_failure)[0]
    if Y_pred == 0:
        return {"FUTUR_DEATH":'NO',"prediction":str(Y_pred)}
    else :
        return {"FUTUR_DEATH":'YES',"prediction":str(Y_pred)}
    
# Using Get
@app.get('/predictLogisticRegression/{age}/{anaemia}/{creatinine_phosphokinase}/{diabetes}/{ejection_fraction}/{high_blood_pressure}/{platelets}/{serum_creatinine}/{serum_sodium}/{sex}/{smoking}')
async def predictLogisticRegression(age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking):
    heart_failure = pd.DataFrame({
    'age': [float(age)],
    'anaemia': [float(anaemia)],
    'creatinine_phosphokinase': [float(creatinine_phosphokinase)],
    'diabetes': [float(diabetes)],
    'ejection_fraction': [float(ejection_fraction)],
    'high_blood_pressure': [float(high_blood_pressure)],
    'platelets': [float(platelets)],
    'serum_creatinine': [float(serum_creatinine)],
    'serum_sodium': [float(serum_sodium)],
    'sex': [float(sex)],
    'smoking': [float(smoking)]
    })
    Y_pred = modelLogisticRegression.predict(heart_failure)[0]
    
    if Y_pred == 0:
        return {"FUTUR_DEATH":'NO',"prediction":str(Y_pred)}
    else :
        return {"FUTUR_DEATH":'YES',"prediction":str(Y_pred)}
    

        
if __name__ == '__main__' :
    uvicorn.run(app,host="0.0.0.0",port="8000")
