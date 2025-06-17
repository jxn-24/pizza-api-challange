# 🍕 Pizza Restaurant RESTful API (Flask)
A Flask-based RESTful API for managing restaurants , pizzas , and their associations (restaurant_pizzas ) with full CRUD operations and validation.

# 🧰 Project Overview
This project provides a RESTful API for a pizza restaurant system where users can:

List all restaurants
Get details of a specific restaurant
Delete a restaurant
List all pizzas
Create an association between a pizza and a restaurant (with price validation)

# 📦 Prerequisites
Make sure you have the following installed:

Python 3.x
Pipenv (for virtual environment)
SQLite (default DB)
Postman (for testing the API)

# 🧪 Technologies Used
Flask – Web framework
Flask-SQLAlchemy – ORM for database interaction
Flask-Migrate – For database migrations
Marshmallow – For request validation

# 🔧 Setup Instructions
 1. Clone the repository
    1. git clone https://github.com/your-username/pizza-api-challange.git 
    2. cd pizza-api-challange

2. Install dependencies using Pipenv
    1. pipenv install flask flask_sqlalchemy flask_migrate marshmallow marshmallow-sqlalchemy


3. Activate the virtual environment
      pipenv shell


# 🗃️ Database Setup
1. Set Flask app environment variable
     export FLASK_APP=server.app

2. Initialize Flask-Migrate
     flask db init

3. Generate initial migration
     flask db migrate -m "Initial migration"

4. Apply migration to create the database
     flask db upgrade


# 🌱 Seed the Database
Run the seeder script to populate sample data:
     python server/seed.py

This will insert:
   -3 sample restaurants
   -3 sample pizzas

# ▶️ Run the App
Start the Flask development server:
     flask run

By default, the app runs on:
👉 http://localhost:5000

# 🧪 Test the API Using Postman
1. Import Postman Collection
  Open Postman → Click Import → Upload:
     pizza-api.postman_collection.json
  You’ll see a folder named "Pizza API" with pre-configured endpoints.