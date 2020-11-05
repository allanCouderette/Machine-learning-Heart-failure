import pandas as pd
import sklearn
import joblib 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def accuracy(preds, Y):
    return (preds == Y).sum() / len(Y) * 100

heart_failure = pd.read_csv('heart_failure_clinical_records_dataset.csv')

X = heart_failure.drop(columns=['time','DEATH_EVENT'])
Y = heart_failure['DEATH_EVENT'].astype('category')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.3, stratify=Y,random_state=2)

model = RandomForestClassifier(max_depth=2, n_estimators=5, random_state=2)
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

print(accuracy(Y_pred,Y_test))
joblib.dump(model, 'modelRandomForest.pkl')