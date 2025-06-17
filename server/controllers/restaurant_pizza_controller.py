from flask import Blueprint, request, jsonify, abort
from marshmallow.exceptions import ValidationError
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server import db

bp = Blueprint('restaurant_pizza_controller', __name__)

@bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = int(data['price'])
        pizza_id = int(data['pizza_id'])
        restaurant_id = int(data['restaurant_id'])

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza or not restaurant:
            abort(400, description="Invalid pizza or restaurant ID")

        rp = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        rp.validate_price()  # custom validation

        db.session.add(rp)
        db.session.commit()

        return jsonify({
            'id': rp.id,
            'price': rp.price,
            'pizza_id': rp.pizza_id,
            'restaurant_id': rp.restaurant_id,
            'pizza': {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            },
            'restaurant': {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
        }), 201

    except (ValueError, KeyError) as e:
        abort(400, description=f"Missing or invalid field: {str(e)}")
    except ValidationError as ve:
        abort(400, description=ve.messages[0])