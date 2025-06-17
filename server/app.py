from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import db from server package and initialize with the app
from server import db
db.init_app(app)  # <-- Important!

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import models (to register them with SQLAlchemy)
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

# Register Blueprints
from server.controllers.restaurant_controller import bp as restaurant_bp
from server.controllers.pizza_controller import bp as pizza_bp
from server.controllers.restaurant_pizza_controller import bp as restaurant_pizza_bp

app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

if __name__ == '__main__':
    app.run(debug=True)