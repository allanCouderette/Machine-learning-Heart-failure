import streamlit as st
import pandas as pd
import sklearn
import joblib

age = st.text_input("age :", "")
anaemia = st.text_input("anaemia :", "")
creatinine_phosphokinase = st.text_input("creatinine_phosphokinase :", "")
diabetes = st.text_input("diabetes :", "")
ejection_fraction = st.text_input("ejection_fraction :", "")
high_blood_pressure = st.text_input("high_blood_pressure :", "")
platelets = st.text_input("platelets :", "")
serum_creatinine = st.text_input("serum_creatinine :", "")
serum_sodium = st.text_input("serum_sodium :", "")
sex = st.text_input("sex :", "")
smoking = st.text_input("smoking :", "")

modelLogisticRegression = joblib.load("modelLogisticRegression.pkl")
modelRandomForest = joblib.load("modelRandomForest.pkl")

if (age and anaemia and creatinine_phosphokinase and diabetes and ejection_fraction and high_blood_pressure and platelets and serum_creatinine and serum_sodium and sex and smoking ) :
    
    conn = psycopg2.connect("host=127.0.0.3 dbname=demo user=allan password=allan")
    cur = conn.cursor()

    query = "INSERT INTO users VALUES (DEFAULT,"
    query = query + str(row['age'])+","

    if row['anaemia'] == 0 :
        query = query + "TRUE,"
    else :
        query = query + "FALSE,"

    query = query + str(row['creatinine_phosphokinase'])+","

    if row['diabetes'] == 0 :
        query = query + "TRUE,"
    else :
        query = query + "FALSE,"

    query = query + str(row['ejection_fraction'])+","

    if row['high_blood_pressure'] == 0 :
        query = query + "TRUE,"
    else :
        query = query + "FALSE,"

    query = query + str(row['platelets'])+","
    query = query + str(row['serum_creatinine'])+","
    query = query + str(row['serum_sodium'])+","

    if row['sex'] == 0 :
        query = query + "TRUE,"
    else :
        query = query + "FALSE,"

    if row['smoking'] == 0 :
        query = query + "TRUE,"
    else :
        query = query + "FALSE,"

    query = query + str(row['time'])+","

    if row['DEATH_EVENT'] == 0 :
        query = query + "TRUE)"
    else :
        query = query + "FALSE)"

    cur.execute(query)
    conn.commit()

    
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
        st.text("RandomForest : NO")
    else :
        st.text("RandomForest : YES")
        
    Y_pred = modelLogisticRegression.predict(heart_failure)[0]
    if Y_pred == 0:
        st.text("LogisticRegression : NO")
    else :
        st.text("LogisticRegression : YES")
    
    
else :
    st.text("Remplis tous les champs")
    