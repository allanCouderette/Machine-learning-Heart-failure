import csv
import psycopg2
import pandas as pd

conn = psycopg2.connect("host=172.28.1.4 dbname=demo user=allan password=allan")
cur = conn.cursor()
cur.execute('DROP TABLE users')
conn.commit()
cur.execute("""
    CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    age text,
    anaemia boolean,
    creatinine_phosphokinase integer,
    diabetes boolean,
    ejection_fraction integer,
    high_blood_pressure boolean,
    platelets double precision,
    serum_creatinine real,
    serum_sodium integer,
    sex boolean,
    smoking boolean,
    time integer,
    DEATH_EVENT boolean
)
""")
conn.commit()

heart_failure = pd.read_csv('../data/heart_failure_clinical_records_dataset.csv')
for index,row in heart_failure.iterrows():
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

    print(query)
    cur.execute(query)
    conn.commit()