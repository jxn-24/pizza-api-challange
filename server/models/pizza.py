from server import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(300), nullable=False)

    # Relationship
    restaurants = db.relationship('RestaurantPizza', backref='pizza', cascade="all, delete-orphan")