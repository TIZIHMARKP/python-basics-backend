# ==================  QUESTIONS ====================

# 1. What is HTTP, how does it work, and what are the major components of an HTTP response?

# 2. What are the common HTTP methods and their purposes?

# 3. Explain the concept of statelessness in HTTP.

# 4. What is the purpose of HTTP headers?

# 5. Describe the status code categories (1xx, 2xx, 3xx, 4xx, 5xx).

# 6. What is the significance of the 200 and 404 status codes?

# 7. How do query strings work in HTTP?

# 8. What are the basic steps to set up a Flask application?

# 9. Explain the role of the Flask app instance.

# 10. What is the function of the `__name__ == "__main__"` check?

# 11. How can environment variables be used to configure Flask?


# =================  ANSWERS =============
"""
Q 1. a. HTTP (HyperText Transfer Protocol) is the protocol used for communication between web clients (like browsers) and servers. It acts as the foundation of data communication on the World Wide Web. 
b. HTTP works on a request-response cycle, where by a client sends a HTTP request, and the server returns a HTTP response. It works as follows
- Client sends a request through a browser or app asking for a resource (like rendering a particular page)
- The server processes or understands what was asked and fetches the data
- Server replies with the requested data or an error message 
- The browser receives the response and displays it to the user
c. The major components of an HTTP response are:
1. Status Line. This is the first line of the response that includes the HTTP version, status code and status message
2. Headers. They are key value pairs that provide additional information about the response. It is usually sent before the body and contains meta data like Content-Type, Set-Cookie, Content-Length
3. Body. It is the actual data being sent by the server. It could be JSON, files, plain text, images or html for web pages.

Q 2. 
The common HTTP methods and their purposes are:
1. GET. The purpose is to retrieve data from the server (read-only)
2. POST. Send data to the server to create a new resource
3. PUT. To update or replace an existing resource entirely
4. DELETE. Removes a resource from the server
5. PATCH. It functions to partially update an existing resource
6. HEAD. It is similar to GET but returns only headers without a body
7. OPTIONS. It ask the server which HTTP methods are allowed for a resource 

Q 3. 
Statelessness in HTTP means that each request from a client to a server is treated as an independent or isolated transaction. The server does not store any information about the client's previous requests. Every request which a client sends must always contain all the data needed for the server to understand and process it. 
Let's take for example we are ordering food at a restaurant, we order our food, we leave. The next day, the server would not remember what we ordered. Every transaction starts fresh every time 

Q 4. 
HTTP headers are used to to pass additional information between the client and server controlling how the request is processed and how the response is interpreted. They provide meta data about the request or response that helps the client and server communicate effectively. The most common purposes include: 
- Authorization. It sends credentials or tokens for authentication
- Content-Type: it tells the client what type of data is in the body (such as text, json)
- Cookie. Functions to transfer stored client data (session IDs)
- Host. Specifying which server the request is for 

Q 5. 
a. 1xx (Informational). It means the request has been received and the server is continuing to process the information.  Example 100 (continue)
b. 2xx (Success). It means the request was successfully received, understood, and accepted by the server. Example 200 (ok), 201 (created)
c. 3xx (Redirection). It means further action is needed from the client to complete the request. Example 301 (Moved permanently), 302 (Found)
d. 4xx (Client Error). It means the request contains bad syntax or it cannot be fulfilled by the client. Example 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found)
e. 5xx (Server Error). It usually means the server failed to fulfill a valid request from the client. Example 500 (Internal Server Error), 502 (Bad Gateway), 503 (Service Unavailable) 

Q 6. 
- Status code 200 stands for OK and indicates that the request was successfully processed and the server is returning the requested content. It is the standard success response for GET requests
- Status code 404 stands for NOT FOUND and indicates that the server cannot find the requested resource. This is one of the most client errors and typically means that the URL is wrong, the page is not available or the resource never existed. 

Q 7.
A query string is a way to send additional data from the client to the server as part of the url appearing with a question mark (?). Example: https://techieversity.africa/learning?course1=backend&course2=frontend. It works as follows
- The client sends the request which the browser or app adds data to the URL after ? 
- The server reads the URL and parses the key value pairs
- The responds by using that data to filter, search and sort the resource

Q 8.
To set up a basic flask application, the following steps are needed
1. Create a project folder and navigate into it
2. Create a virtual environment in your working directory and activate it
3. Install Flask using "pip install flask"
4. Create a Python file (example app.py) with the following
- import Flask
- Create an instance of the Flask class
- Define routes with @app.route()
- Write view functions that return responses
5. Run the app with "python app.py"
6. We access the app in browser at http://127.0.0.1:5000 
"""