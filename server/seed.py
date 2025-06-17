from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Seed restaurants
    r1 = Restaurant(name="Tony's Pizza", address="123 Main St")
    r2 = Restaurant(name="Mama Mia", address="456 Pine Rd")
    r3 = Restaurant(name="Kiki's Pizza", address="789 Oak Ave")

    # Seed pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Cheese, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Cheese, Pepperoni")
    p3 = Pizza(name="Veggie", ingredients="Tomato, Cheese, Peppers, Onions")

    # Add to session and commit
    db.session.add_all([r1, r2, r3, p1, p2, p3])
    db.session.commit()

    print("✅ Database seeded successfully!")