# ===============    QUESTIONS    ================

# 1. What does CRUD stand for in database operations?

# 2. How is data created and saved using SQLAlchemy in Flask?

# 3. What is the function of `db.session.add()`, `db.session.commit()` and `db.session.rollback()`?

# 4. What is the role of `@app.route()` or `@api.route()` in Flask REST APIs?

# 5. Product Inventory API with Error Handling

# Develop a RESTful Flask API to manage a product inventory, with robust error handling and JSON responses, stored in a PostgreSQL database. Push to Github

# Requirements:

# Performing CRUD Operations: Set up a PostgreSQL database with a products table (columns: id (serial), name (varchar), price (numeric), stock (integer)).


# API in Flask – REST II & III:

# Create RESTful routes:GET /api/products: Return a JSON list of all products.

# GET /api/products/<id>: Return a single product by ID.

# POST /api/products: Create a product (JSON payload: name, price, stock).

# PUT /api/products/<id>: Update a product’s details (allow partial updates).

# DELETE /api/products/<id>: Delete a product by ID.

# Use proper HTTP status codes (e.g., 201 for created, 404 for not found, 400 for invalid data).

# Implement input validation (e.g., price and stock must be non-negative).


# Functionality:

# Connect to MySQL and execute SQL queries for CRUD operations.

# Return JSON responses (e.g., {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10}).

# Handle errors with try-except (e.g., database errors, invalid JSON, non-existent IDs) and return JSON error messages (e.g., {"error": "Product not found"}).

# Log all API requests and errors to a file using the logging module.

# Structure the app with app.py, a database.py module for DB operations, and static/ for optional CSS.

# Add a /api/products/search route that accepts a query parameter (e.g., /api/products/search?name=laptop) to filter products by name (case-insensitive).

# ================== ANSWERS ================
# Q1. CRUD stands for Create, Read, Update, and Delete and these are the four fundamental operations which can be used to manage data in a database. 
# - Create inserts a new data into a database
# - Read retrieves existing data from a database
# - Update modifies an existing data in a database
# - Delete removes an existing data from a database
# CRUD operations are the foundations of most backend applications

# Q2. In Flask SQLAlchemy, to create data, it relies on the Object Relational Mapping patter (ORM). Instead of writing raw SQL queries database records are created as standard python class instances and they are saved to the database using the db.session object. It has the following key steps from data being created to data being saved: 

# 1. We define the database model. A model is a python class that inherits from db.Model which defines the structure of the database table (columns, datatypes, and constraints) using db.Column 
# 2. We instantiate the Model (Create the Record). New records are created by instantiating the model class with key value arguments which represent column values. The object at this stage exists only in python memory and has not yet been added to the database yet
# 3. We add the object instance to the Session. The database object instance is added to the session using db.session.add() which acts like the staging area tracking pending changes to be added to the database. For multiple records, we use db.session.add_all([example1, example2])
# 4. Lastly, we commit the session.  The changes are save permanently with db.session.commit(), and this converts the python object operations into an SQL INSERT statement. After it has been commited, fields are generated (like primary key) in SQLAlchemy. 

# The following example shows how data is created and saved  using SQLAlchemy: 
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# class Assingment(db.Model):  # Defining the model (table)
#     id = db.Column(db.Integer, primary_key=True)
#     course = db.Column(db.String(100), nullable=False)
#     task = db.Column(db.Integer, nullable=False)

# new_task = Assingment(course="Backend", task=9) # creating an instance object
# db.session.add(new_task)  # Adding to session
# db.session.commit()       # Saving to database


# Q3. 1. db.session.add(). It stages an object for insertion into the database or updates the session of a database with a new record. No database change occurs in the database until the commit() function is called, it just adds the object to pending in the session

# 2. db.session.commit(). It is used to permanently save all pending changes (such as inserts, updates, deletes) to the database thereby making all staged changes permanent. If any error occurs during the process, the instruction is rollback

# 3. db.session.rollback(). It is used when an error occurs or when we want to discard changes. It cancels all pending changes and reverses previous sessions to their last committed state. Furthermore, it prevents partial or inconsistent data from being saved

