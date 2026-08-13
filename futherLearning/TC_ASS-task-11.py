# ================= QUESTIONS =========================

# 1. What is the importance of testing in software development? Describe the difference between unit testing and integration testing.

# 2. What is the purpose of debugging? How do you use `print()` for simple debugging in Python? What is `pytest` and how is it used?

# 3. How do you test Flask routes?

# 4. What is the role of environment variables during deployment?

# 5. Todo List API with Basic Authentication

# Build a RESTful Flask API for a todo list, using Blueprints for modularity and basic authentication, with tasks stored in memory, SQLite or SQL. Push to Github

# Requirements:

# REST III – Todo List & Resources, External API Connection:Create a RESTful API for todos with routes:GET /api/todos: List all todos.

# POST /api/todos: Create a todo (JSON: title, description, completed).

# PUT /api/todos/<id>: Update a todo.

# DELETE /api/todos/<id>: Delete a todo.

# Use an in-memory list, SQLite or SQL for storage (e.g., todos table: id, title, description, completed).

# Connect to an external API (e.g., https://jsonplaceholder.typicode.com/todos) to fetch sample todos on startup and populate the database/list.


# Blueprints, Middleware, Hooks, Authentication, Authorization:

# Use a Flask Blueprint (todo_bp) to organize todo-related routes.

# Implement basic authentication using HTTP Basic Auth (e.g., flask-httpauth) with a hardcoded user (e.g., username: admin, password: secret).

# Add a before_request hook to log all incoming requests (method, path) to a file.


# Functionality:

# Fetch initial todos from the external API using the requests library and store them.

# Require authentication for all API routes, returning 401 for unauthorized access.

# Return JSON responses with appropriate status codes (e.g., 201 for created, 404 for not found).

# Handle errors (e.g., invalid JSON, non-existent ID) with JSON responses.

# Structure the app with app.py, a todo Blueprint module, and static/ for optional UI.

# Add a /api/todos/completed route to return only completed todos, accessible only to authenticated users.

# write a small test suite for at least one endpoint


# =================== ANSWERS ====================

# Q1. Testing which is the process of verifying that our software works as expected, is free of bugs and meets user requirements, is essential in software development because of the following reasons
# - It Ensures Reliability and Quality. Without testing, it will be difficult to know if an application works as it is suppose to work, but testing guarantees that the application functions according to the business requirements and user expectations under all the expected conditions
# - Prevents costly defects. It is more easier and faster to catch or discover bugs in the early stages of the development lifecycle than it is to fix them during security breaches in production
# - It further serves as executable documentation. Clear test cases demonstrates how individual units, functions, and API routes are supposed to be called and how they handle edge cases which further improves developers experience
# - Lastly but not the least, testing in software development improves maintainability and developer speed which allows developers to ship all changes with confidence thereby reducing time spent on bugs or errors requiring emergency
# The difference between Unit testing and Integration testing are: 
# - Unit testing tests individual components in isolation while Integration testing tests how multiple components work together, using real dependencies like databases or APIs
# - Furthermore, Unit testing testing is fast, easy to write and catches logic errors whereas Integration testing takes time to ensure all different components work together and it catches interaction errors between the components. 



