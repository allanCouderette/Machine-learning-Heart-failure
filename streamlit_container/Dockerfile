FROM python:3.8-slim
WORKDIR /app
COPY . /app
ADD heart_failure_clinical_records_dataset.csv /app
RUN pip3 install -r requirement.txt
EXPOSE 8000

CMD python3 algoRandomForest.py && python3 algoLogisticRegression.py && streamlit run web.py