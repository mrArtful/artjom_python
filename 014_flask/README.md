# Flask Tutorial

This folder contains a step-by-step guide to learning Flask.

## Steps:

1.  **`01_hello_world.py`**: The simplest Flask application. Learn about the `Flask` class and basic routing.
2.  **`02_routing.py`**: Advanced routing, including variable rules (`<username>`, `<int:post_id>`).
3.  **`03_templates.py`**: Rendering HTML using Jinja2 templates. Learn how to pass data to templates and use loops/conditionals.
4.  **`04_forms_and_methods.py`**: Handling GET and POST requests. Learn how to process data from an HTML form.
5.  **`05_static_files.py`**: Serving CSS files and using template inheritance (`{% extends %}`) to keep your code DRY.
6.  **`06_json_api.py`**: Building a basic JSON API. Learn how to use `jsonify()` to return data for mobile apps or frontends.
7.  **`07_redirects_and_errors.py`**: Handling redirects (`redirect`, `url_for`) and custom error pages (like a custom 404 page).
8.  **`08_database_basics.py`**: Connecting Flask to a SQLite database. Learn how to save and retrieve persistent data.

## How to run:

1.  Ensure the virtual environment is activated.
2.  Run any script: `python 01_hello_world.py`
3.  Open your browser at `http://127.0.0.1:5000/`
