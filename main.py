from fastapi import FastAPI, HTTPException
from model import TitanicModel
from input import PassengerData

app = FastAPI()

model = TitanicModel("./models/titanic_decision_tree_model.pkl")

@app.get("/")
async def index():
    return {"message": "Hello World!"}

@app.post("/predict")
async def predict(data: PassengerData):
    try:
        result = model.predict(data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))