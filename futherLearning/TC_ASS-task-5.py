#      =========== QUESTION ==============

# 1. What are advanced data types in Python and why are they useful?

# 1. Describe the difference between list vs tuple and set vs dictionary.

# 3. Write a program that creates two sets of numbers, finds their intersection and union, and prints the results.

# 4. Write a program that defines a nested dictionary representing a classroom (e.g., { "class1": {"Alice": 85, "Bob": 90}, "class2": {"Charlie": 78}}). Create a function to calculate the average score for each class and return a dictionary with class names and their averages.

# 5. What is Flask and why is it used in web development?

# 6. Describe the request-response cycle in a Flask application.

# 7. How does Flask handle incoming HTTP requests?

# 8. What is the `flask run` command used for?


#      =========== ANSWERS ==============

# 1. Advance data types in python are a special collections of structures which are designed to store, organize and manipulate data more efficiently thereby offering extra functionality, better performance and manipulation of data for more specific use cases. 
# Example include List and Tuples. They are useful because of the following reasons
# - Performance. Advance data types in python are optimized for speed
# - Readability. It makes code easier to read
# - Efficiency. It provides a more easier or less way to write code
# - Safety. If further prevents errors from occurring 

# 2. A. List vs Tuples: 
# - A list is a mutable (modifiable) collection of elements. On the other hand, a tuple is an immutable (non - modifiable) collection of elements
# - List generally consume more memory while tuples uses less memory
# - List are stored using square brackets (example, [1, 2, 3]) while tuples are stored using parentheses (example, (1, 2, 3))
# - List are used when data changes often while tuples are used when data stays constant

# B. Set vs Dictionary:
# - A set is an unordered collection of unique elements while a dictionary is a collection of key-value pairs in which the keys are unique, and values can be of any data type
# - Set uses curly braces (example, {1, 2, 3} as the syntax while dictionary uses curly braces with colons (example, {"a": 1, "b": 2})
# - In set, no duplicates are allowed whereas in dictionary keys must be unique but values can repeat 

# 3. Write a python program that creates two sets of numbers, finds their intersection and union, and prints the results.

# =================== SOLUTION =========================
# set_World = {1, 2, 3, 4, 5, 6, 7, 8, 9, }
# set_Africa = {3, 4, 5, 10}

# print("Union: ", set_World.union(set_Africa))          # Output: {1, 2, 3, 4, 5}
# print("Intersection: ", set_World.intersection(set_Africa))   # Output: {3}


# 4. Write a program that defines a nested dictionary representing a classroom (e.g., { "class1": {"Alice": 85, "Bob": 90}, "class2": {"Charlie": 78}}). Create a function to calculate the average score for each class and return a dictionary with class names and their averages.

# classRoom = {
#     "Form1": {"Alice": 85, "Bob": 90, "Mary": 88, "John": 70},
#     "Form2": {"David": 80, "Adam": 92, "Rice": 50},
#     "Form3": {"Burinyu": 70, "Tata": 75},
#     "Form4": {"Randy": 80}
# }

# def calcuAvg(classes):
#     avgs = {}

#     for className, studs in classes.items():
#         scores = studs.values()
#         avg = sum(scores) / len(scores)
#         avgs[className] = round(avg, 2)

#     return avgs

# AvgResult = calcuAvg(classRoom)
# print("Final Average Result: ", AvgResult)


# 5. Flask is a web application framework written in python based on the werkzeug WSGI toolkit and jinja2 template engine. It is designed to be lightweight, flexible and easy to navigate. It is used in web development because of the following reasons
# - Easy to learn with simple syntax
# - Flexible and lightweight as compared to Django
# - Flask further makes it easy for building REST APIs  


# 6. The request-response cycle in a Flask application is the flow from when a user sends a request to the time the server responds to that request. It functions like a real conversation when a user ask for something (request) and the server (flask application) listens, understands, process and response. The cycle is as describe below

# - User sends a specific request to a specific URL
# - The flask development server receives the raw http request and converts it into a python object
# - Flask matches the routes by looking at the request URL and http method and finds the corresponding route which the user specified
# -  A request object is created by flask containing all the data sent by the client such as url parameters, headers, json data and so on
# - The view function is executed by flask by calling the function inside the route executing that specific task. Inside this function, the user can access request data, perform logic or can call other functions. 
# - The response is then generated and flask converts it into an http response and adds status code, headers and body (depending on the content returned)
# - The response is then sent back to the client through the browser, which renders html, displays a message or handles json data

# 7. Flask handle incoming http requests by following a structured approach that transforms raw http data into a usable python object, routes them to the correct function, and returns back a response. Let's take for example that we have a waiter at a busy restaurant
# - a customer arrives (http request) at a restaurant, and the waiter ask what they need as food (url routing), looks for the right food (view function) and gives a reply (response), then finally packages it and hands the food to the customer (http response)
# - This is handle in flask through a WSGI server that passes the raw request to Flask which wraps the request, routes the url, executes the view, generates the response and returns the http response back to the client. 

# 8. The flask run command is used to start the built-in development server for a Flask application. It starts the local web server (by default on localhost 5000) so we can test and preview our application during development.

