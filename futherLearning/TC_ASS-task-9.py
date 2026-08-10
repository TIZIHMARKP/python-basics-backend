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
# 1. CRUD stands for Create, Read, Update, and Delete and these are the four fundamental operations which can be used to manage data in a database. 
# - Create inserts a new data into a database
# - Read retrieves existing data from a database
# - Update modifies an existing data in a database
# - Delete removes an existing data from a database
# CRUD operations are the foundations of most backend applications


                                                                 