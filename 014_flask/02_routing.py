from flask import Flask

app = Flask(__name__)

# Basic route
@app.route('/')
def home():
    return '<h1>Home Page</h1><p>Try going to /user/Artjom or /post/5</p>'

# Route with a string variable
# The <username> part is a placeholder. Flask passes it as an argument to the function.
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

# Route with an integer variable
# You can use converters like <int:post_id> to ensure the variable is of a specific type.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # post_id is now an integer
    return f'Post ID: {post_id} (Type: {type(post_id)})'

# Routes can also handle multiple path segments
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'

if __name__ == '__main__':
    app.run(debug=True)
