import csv
import psycopg2
import pandas as pd

conn = psycopg2.connect("host=172.28.1.4 dbname=demo user=allan password=allan")
cur = conn.cursor()
cur.execute('SELECT * FROM users')

mobile_records = cur.fetchall() 

with open('heart_failure_clinical_records_dataset_EXPORT.csv','w') as f:
    wr = csv.writer(f)
    wr.writerow(['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time','DEATH_EVENT'])
    for row in mobile_records:
        wr.writerow([str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9]),str(row[10]),str(row[11]),str(row[12]),str(row[13])])