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

# Q2. Debugging is the process of finding, analyzing and fixing errors or unintended behaviors in software code with the main purpose of ensuring that software operates correctly, reliably and according to specifications of the application by removing the problems of failures. The main objectives of debugging are: 
# - To detect logical errors
# - To identify all runtime errors
# - To verify all state changes and variable values at specific execution steps thereby reducing application downtime and increasing application stability 

# print() is used in the following ways for debugging in python:
# - print() is inserted inside conditions or loops to verify which branches execute
# - print() is used to inspect state during debugging by printing variable values before and after operations to see or know where data changes unexpected
# - print() can further be used for debugging by making use of the python f-string debugging syntax `print(f"{variableName=}" variableValue")`  to print both the variable name and its value automatically

# `pytest` is a python testing framework which is used to write and run automated tests. It can be used by following the various steps below
# 1. Install pytest by using the command 'pip install pytest'
# 2. Test files are created which starts with test_ or ending with _test.py
# 3. Test functions are written which stars with test_ 
# 4. `assert` is used to check expected results in the function
# 5. The program is executed by running the `pytest` command in the command line

# Q3. Testing a route in flask can be done using the built-in test client (app.test_client()) which simulates HTTP requests when the server has not been started. 
# - The first step is to create a test client using client = app.test_client()
# - The second step is to send a requests using client.get() or any other HTTP method
# - We then check the status response and json response using assert

# Q4. Environment variables roles during deployment include: 
# - Security and secret management. Sensitive credentials such as database passwords, API keys, encryption keys must never be hardcoded into source code or committed to Git repositories
# - Environment separation. Environment variables play a key role for having different configurations settings for an application base on which stage it is running such as development stage, testing or production stage but still keeping similar or identical code
# - Portability. Environment variables play a role to make it possible to be able to run same code in any environment stage
# - Again, environment variables gives flexibility during deployment as developers are just required to change configurations without the need to redeploy  
