# =================== TASK 7 QUESTIONS ==========================

# 1. What is routing in Flask and why is it important?

# 2. What are best practices for organising routes in a Flask application?

# 3. How can parameters be passed in URLs?

# 4. Explain the purpose of template rendering in web applications.

# 5. Blog Platform with Category Pages

# Develop a Flask blog application with category-based routing, using Jinja2 templates for rendering posts and static files for styling and images. Push to Github

# Requirements:

# A. Routing and Application Structure:

# - Create routes: / (home), /blog, /category/<category_name>, and /post/<post_id>.

# - Structure the app with templates/, static/css/, and static/images/ folders.

# - Store blog posts in a Python list or dictionary (e.g., posts = [{"id": 1, "title": "Post 1", "category": "Tech", "content": "..."}, ...]).

# B. Jinja2 Templates & Static Files:

# i. Use a base.html template with a header, footer, and navigation bar.

# ii. Create templates: home.html (welcome page), blog.html (list all posts), category.html (filter posts by category), and post.html (individual post details).

# iii. Style the app with static/css/blog.css (e.g., card layout for posts, hover effects).

# iv. Include a static image (e.g., a blog banner) in static/images/ displayed on the home page.

# C. Functionality:

# - Home: Show a welcome message and a banner image.

# - Blog: Display all posts with titles and summaries using a Jinja2 loop.

# - Category: Filter posts by category (e.g., "Tech", "Lifestyle") and display matching posts.

# - Post: Show full post details for a given post_id.

# - Handle invalid routes (e.g., non-existent post ID or category) with a custom 404 template.

# - Add a /search route that accepts a query parameter (e.g., /search?q=python) and renders a template showing posts containing the query in their title or content.


# =================== TASK 7 ANSERS ==========================

# 1. Routing in Flask is the process that maps a URL to a specific python function (which is often called the view function) in a flask application. It is defined using the @app.route() decorator which tells our Flask application which function to call when a specific URL is requested by a user. 

# Routing in Flask is important for the following reasons:
# - It Organizes code. Routing separates our application logic by URL thereby making it easier to manage and maintain
# - It supports dynamic content. We can create flexible URLs that accept parameters such as: @app.route('/post/<int:post_id>') in a flask application
# - Routing in flask supports different HTTP methods, making it possible to route the same URL but handle different methods like GEt, POST, DELETE. 
# -  Routes further allows us to map our application's structure logically so that users can navigate easily thereby improving users experience
# - To conclude, routing is important for building RESTFUL APIs in Flask applications

# 2. Best practices for organising routes in a Flask application: 
# - Make use of blueprints for modularity. Blueprints allows us to group related routes, templates, and static files in a reusable module which keeps code clean and organized
# - We should always separate routes from application logic by moving the application logic to services
# - Organize routes by features or domain and not by their HTTP methods
# - Routes functions should be kept short. Each route should do one thing or have one responsibility
# - Routes should be named descriptively making it easy for programmers to understand what each routes do
# - Document your routes by using comments or readme to explain what each routes does
# - Use consistent response formats like JSON or HTML formats to show the outcome of a request 
# - Furthermore, declare which HTTP methods are to be used in a specific routes to avoid errors
# - Last but not the list, validate users input data in the route function to ensure only the required or correct data is send by the user

# 3. Parameters can be passed in URLs in two main ways which are: 
# A. URL Path Parameters: These are values which are part of the URL path itself that are used to identify specific resources (like a user with a specific IDD).
# - Examples are: /users/43, /posts/2026/flask-routing, 
# - It is used when identifying a specific resource, creating clean SEO urls or when the parameter is essential to the route structure

# B. Query String Parameters: These are string parameters which appear after a question mark (?) and separated by &. They are used for filtering, searching pagination and optional data
# - Example: /assignment?task=7&q=5, /users?page=7&name=tizih


# 4. Template rendering in web applications is the process of generating dynamic HTML pages by combining static HTML structure with dynamic data from the server before they are send to the client browser. It is important because of the following purposes
# - Separations of concerns. It makes it possible to to keep presentation template (HTML) from business logic (python code)
# - Reusability. A single template can be used for multiple pages in a web application
# - Template rendering displays data from databases, APIs or users input thereby making them dynamic with content
# - Template rendering enhances maintainability as a single change in one HTML page updates everywhere
# - HTML structure is clear and easy to understand. This makes it easy to read

# 5. https://github.com/TIZIHMARKP/flask-blog-platform.git
