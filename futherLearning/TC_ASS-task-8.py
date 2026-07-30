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

# 2. The request object in flask represents the current incoming HTTP request sent by a client through a web browser or API request. It is the primary way which all Flask applications retrieve client data, including form submissions, query parameters, json payloads, file uploads, headers and cookies. The main roles include:
#  - Accessing form data from POST requests by making use of request.form
# - Accessing URL query parameters using the request.args attribute
# - Getting all request HTTP methods using request.method attribute
# - Accessing JSON data from API requests through the request.get_json() attribute
# - Accessing cookies through the request.cookies attributes
# - Last but not the least, it further access all uploaded files using the request.files attribute

# 3. Form handling comes with several security concerns which when handled properly protects users and data. Some of these security concerns include:
# - Cross-Site Scripting (XSS). Attackers inject malicious javascript into users form fields. When the data is displayed without being sanitized, the script runs in other user's browsers, which may potentially steal cookies, session data, or performing actions on behalf of the user. It can be prevented by sanitizing input
# - Cross-Site Request Forgery (CSRF). It is a scenario where attackers trick authenticated users to submit a form they didn't intend to submit. The form sends a request to the users application with the user's session, allowing the attacker to perform actions without the user's consent. It can be prevented by the use of CSRF tokens where a unique token for each form is generate and validated
# - SQL Injection. It is a situation in which hackers or attackers inject malicious sql queries through form data. It can be prevented using an ORM like SQLAlchemy
# - File Upload Vulnerabilities. It is the upload of malicious files that could execute code on a user server. It can be prevented by validating file types (extensions), limiting file size or renaming uploaded files
# - Log Injection. It is a situation whereby an attacker submit data that corrupts logs thereby making them harder to read or injecting malicious log entries.



