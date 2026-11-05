from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("sales_model.pkl")

@app.get("/predict")

def predict(marketing_spend:int, season:int, region:int):

    df = pd.DataFrame([{
        "marketing_spend": marketing_spend,
        "season": season,
        "region": region
    }])

    pred = model.predict(df)

    return {"predicted_sales": float(pred[0])}