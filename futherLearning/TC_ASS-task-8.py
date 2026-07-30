# ========= QUESTIONS =============
# 1. How does Flask handle form data sent through HTTP requests?

# 2. What is the role of the `request` object in Flask?

# 3. What security concerns are associated with form handling?

# 4. Describe the use of `request.args` and `request.form`.

# 5. Explain the differences between SQL and NoSQL databases.

# ======= ANSWERS ===================

# 1. Flask handles form data by making use of the global request object which is imported from the flask module. 
# - The handling of the form data by flask depends on the HTTP methods, the requests content-Type header and the data format

# i. Standard HTML Form Submissions
# - When an HTML form is submitted using the POST method with the standard content type, the the data is accessed in flask through the request.form method. The request.form is an immutable multi Dictionary key pair which supports multiple values per key.
# - One of the best practices to retrieve the data using flask function is by making use of the request.form.get('key") logic, as the .get() would return None if the key is  not present rather than giving us a bad request error 404.
# - When checkboxes or multiple select dropdown menus are sharing the same name attribute, the request.form.getlist('key') is usually used to return a list of all the submitted values. 
# ii File Uploads
# - When ever a form data is submitted using input type="file", the files are separated from text fields and stored in request.files by flask request objects. Each entry in request.files is a file storage object which are then save to disk using the .save() python method
# iii. Data Format (JSON Form submissions)
# - When form data is submitted through APIs as json format, data is accessed using request.get_json() or request.json. Flask handles the json data by parsing the raw json string into a python dictionary
# iv. Query Parameters (GET requests)
# - When form data is appended to the url query string, data is retrieved using request.args.get('key')


