import joblib

from unicodedata import category
import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Predicting Fraud")


# Represents a particular wine (or datapoint)
class Transaction(BaseModel):
    Time: int
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


@app.on_event("startup")
def load_clf():
    # Load classifier from pickle file
    with open("/app/xgb.pkl", "rb") as file:
        global clf
        clf = joblib.load(file)


@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http://localhost:80/docs"


@app.post("/predict")
def predict(tran: Transaction):
    data_point = pd.DataFrame(
        [
            {
                'Time': tran.Time,
                'V1': tran.V1,
                'V2': tran.V2,
                'V3': tran.V3,
                'V4': tran.V4,
                'V5': tran.V5,
                'V6': tran.V6,
                'V7': tran.V7,
                'V8': tran.V8,
                'V9': tran.V9,
                'V10': tran.V10,
                'V11': tran.V11,
                'V12': tran.V12,
                'V13': tran.V13,
                'V14': tran.V14,
                'V15': tran.V15,
                'V16': tran.V16,
                'V17': tran.V17,
                'V18': tran.V18,
                'V19': tran.V19,
                'V20': tran.V20,
                'V21': tran.V21,
                'V22': tran.V22,
                'V23': tran.V23,
                'V24': tran.V24,
                'V25': tran.V25,
                'V26': tran.V26,
                'V27': tran.V27,
                'V28': tran.V28,
                'Amount': tran.Amount
            }
        ]
    )
    pred = clf.predict(data_point)
    if pred[0] > 0.5:
        prediction = "Fraud"
    else:
        prediction = "Not Fraud"
    print(prediction)
    return {"Prediction": prediction}
