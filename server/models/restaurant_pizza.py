from server import db
from marshmallow import ValidationError

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def validate_price(self):
        if not (1 <= self.price <= 30):
            raise ValidationError("Price must be between 1 and 30")