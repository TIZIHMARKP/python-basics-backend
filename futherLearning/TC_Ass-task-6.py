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

Q3. 
Statelessness in HTTP means that each request from a client to a server is treated as an independent or isolated transaction. The server does not store any information about the client's previous requests. Every request which a client sends must always contain all the data needed for the server to understand and process it. 
Let's take for example we are ordering food at a restaurant, we order our food, we leave. The next day, the server would not remember what we ordered. Every transaction starts fresh every time 


"""