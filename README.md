# House Price Prediction

## Overview

This project is a house price prediction model. It uses various features of a house to predict its price.

## Features

- **square_meters**: The total area of the house in square meters.
- **floors**: The number of floors in the house.
- **sleeping_rooms**: The number of sleeping rooms in the house.
- **bathrooms**: The number of bathrooms in the house.

## Usage

### Running the Application

1. **Build the Docker image**:
    ```sh
    docker build -t house-price-predictor .
    ```

2. **Run the Docker container**:
    ```sh
    docker run -p 80:80 house-price-predictor
    ```

### Making Predictions

Send a POST request to the `/predict` endpoint with the house features:

```python
import requests

url = "http://localhost:80/predict"
data = {
    "square_meters": 100.0,
    "floors": 2,
    "sleeping_rooms": 3,
    "bathrooms": 2
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())