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


