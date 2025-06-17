from flask import Blueprint, jsonify, abort
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

bp = Blueprint('restaurant_controller', __name__)

@bp.route('/restaurants')
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        'id': r.id,
        'name': r.name,
        'address': r.address
    } for r in restaurants])

@bp.route('/restaurants/<int:id>')
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        abort(404, description="Restaurant not found")

    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [{
            'id': p.pizza.id,
            'name': p.pizza.name,
            'ingredients': p.pizza.ingredients,
            'price': p.price
        } for p in restaurant.pizzas]
    })

@bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        abort(404, description="Restaurant not found")

    Restaurant.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({}), 204