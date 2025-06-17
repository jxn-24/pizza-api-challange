from server import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)

    # Relationship
    pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade="all, delete-orphan")