# =============== TASK 10 QUESTIONS ================

# 1. How do you send requests to an external API in Python and what Python module is used to make HTTP requests?

# 2. What are some common challenges when working with external APIs?

# 3. What is the purpose of Blueprints in Flask?

# 4. What is middleware in web development and how can middleware be implemented in Flask?

# 5. What are Flask hooks and what are they used for? What is the difference between `before_request` and `after_request` hooks?

# 6. Define Authentication and Authorization in the context of web applications. What security practices should be followed when implementing authentication?


# ================= ANSWERS ===================

# Q1. In python, we mostly send requests to an external API by making use of the requests library which provides a simple interface for making HTTP requests and handling responses. 
# - The process usually involves making a HTTP call (either GET, POST, PUT, or DELETE), passing any required parameters, headers or auth tokens and handling the server's response
# - To fetch data from an external API, we use the requests.get(). To pass a query parameter, we make use of the params dictionary and to pass a headers (like API keys), we make use of  headers
# -   To send data to an external API, we use requests.post()
# - The primary python module used to make HTTP requests is the requests library, which is a third party package that requires installation (pip install requests). It handles HTTP interactions, manages sessions and allows for JSON parsing

# Q2. Some of the most common challenges when working with external APIs include
# - Authentication and Authorization complexity. APIs use various security implementations some of which range from simple API keys to complex multi factor flows. Improperly stored API keys can expose sensitive data to leaks.  Furthermore, managing short lived access tokens, refresh tokens and signature generations (like JWTs) also increase code complexity
# - Breaking changes and API versioning. API providers are usually updating their systems and if a provider introduces a breaking change like removing endpoints, renaming JSON keys or changing data types without proper versioning of the APIs, it becomes possible for clients applications to crash with an unexpected runtime error when the external APIs were updated without notice
# - Rate Limiting. External APIs providers usually restrict the number  of requests a client can make within a specific time frame (like100 requests per hour) to prevent server overload and as a result of this, applications can crash or fail to serve users during high traffic 
# - Network Issues and Timeouts. External APIs are accessed over the internet which is unreliable due to network failures or slow responses and timeouts are some of the common challenges experienced
# - Data Volume and Performance. Large amounts of data can be slow to fetch over an external API due to slow pagination over many records and processing overhead


# Q3. In Flask, Blueprints is a way to organize and structure web applications into distinct reusable components or modules. It has the following purposes in flask
# - Modularization. Large applications are difficult to maintain if all routes, databases models and code logic are all kept in a single file. Blueprints allow developers to break down large applications into logical functional modules or components 
# - Code reusability and organization. A blueprint functions like a mini section of an app that can be registered multiple times on the same application under different URL
# - Separation of concerns. Blueprints enable developers to keep different areas of the application separate from each other
# - Collaboration. With blueprints in flask, it makes it easier for multiple developers to work on different areas of an application without conflicts
# - Lastly but note the least, it is easier to test individual components of an application built with flask with the use of blueprints

# Q4. Middleware is software or code that acts as a bridge between an incoming client HTTP request and the server response. It usually sits in the middle of the request response cycle, intercepting incoming requests and outgoing responses to perform additional processing like security checks. 
# In flask, middleware can be implemented using three main ways which are
# 1. Using @app.before_request and @app.after_request. 
# - @app.before_request usually runs code before each request
# - @app.after_request usually runs code after each request
# For example 
# @app.before_request
# def authenticate(): # checking if user is login before giving them access
#     if not session.get('user_id'):
#         return "Please logIn", 401

# @app.after_request
# def add_security_headers(response): # Adding security layers for every response
#     response.headers['X-Frame-Options'] = 'DENY'
#     return response


# 2 Using @app.errorhandler for exception handling. It is used for handling exceptions globally in one place. For example
# @app.errorhandler(404)
# def not_found(error):
#     return jsonify({"error": "Resource not found"})

# 3. By using custom WSGI middleware which wraps the  entire flask application with a WSGI middleware class. For example
# class LoggingMiddleware:
#     def __init__(self, app):
#         self.app = app
#     def __call__(self, environ, start_response):
#         print(f"request: {environ.get('PATH_INFO')}")
#         response = self.app(environ, start_response)
#         print("Response sent")
#         return response

# app.wsgi_app = LoggingMiddleware(app.wsgi_app)


# Q5. Flask hooks are special decorator functions that allows developers to execute code automatically at specific stages in the life cycle of a HTTP request. Flask hooks usually allows developers to run functions automatically before or after a request is processed without the need to call them directly in every route. They are used for the following
# - Authentication and Authorization. It is used to check if a user is login or if a valid API token is present before executing the route handler
# - Error handling. They are used to log errors when an exception occurs during a request execution 
# - Database Connection.  Flask hooks are used for opening a database connection when a request arrives and closing it when the request ends
# - Logging and Analytics. Flask hooks are used for logging request details like endpoint, ip address, timestamp and also used for measuring the duration of a request. 
# The difference between @before_request and after_request hooks lies in their execution timing
# - @app.before_request runs before the route function is called and it has access to the request object but not the response while @app.after_request runs after the route function returns a response and it has access to both the request and response object. 





