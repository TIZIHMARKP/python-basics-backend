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

