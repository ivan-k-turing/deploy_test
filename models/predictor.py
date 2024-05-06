class Predictor:

    def predict(self, square_meters: float, floors: int, sleeping_rooms: int, bathrooms: int) -> float:
        base_price = 50000

        price_per_square_meter = 3000
        price_per_floor = 20000
        price_per_sleeping_room = 15000
        price_per_bathroom = 12000

        predicted_price = (base_price +
                           square_meters * price_per_square_meter +
                           floors * price_per_floor +
                           sleeping_rooms * price_per_sleeping_room +
                           bathrooms * price_per_bathroom)
        return predicted_price
