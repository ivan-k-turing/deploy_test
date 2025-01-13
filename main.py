import pickle

from fastapi import FastAPI

from sklearn.linear_model import LinearRegression

from src.predictor import HouseInfo, Prediction
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI application!"}


with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)


# post method to predict house prices
@app.post("/predict")
def predict_price(request: HouseInfo) -> Prediction:
    features = [[request.square_meters, request.floors, request.sleeping_rooms, request.bathrooms]]
    predicted_price = model.predict(features)[0]
    return Prediction(price=predicted_price)
