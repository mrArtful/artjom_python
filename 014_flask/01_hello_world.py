from flask import Flask

# Create an instance of the Flask class. 
# __name__ is a special variable in Python that tells Flask where to look for resources like templates and static files.
app = Flask(__name__)

# The @app.route decorator tells Flask which URL should trigger our function.
# '/' is the root URL (e.g., http://127.0.0.1:5000/)
@app.route('/')
def hello_world():
    # The function returns the content we want to display in the user's browser.
    return 'Hello, Flask! This is our first web application.'

# The main block ensures that the server only runs if the script is executed directly.
if __name__ == '__main__':
    # debug=True enables the debugger and auto-reloader, making development easier.
    # NEVER use debug=True in a production environment.
    app.run(debug=True)
