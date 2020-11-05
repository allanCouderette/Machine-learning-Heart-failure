import csv
import psycopg2
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
with open('../data/heart_failure_clinical_records_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Ne pas faire le header
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (DEFAULT,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        row
    )
conn.commit()