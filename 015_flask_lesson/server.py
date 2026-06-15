from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    user_data = {
        'name': 'Roman',
        'title': 'My Flask App',
        'items': ['Learn Python', 'Learn Flask', 'Build a website'],
    }

    print(url_for('static', filename='styles.css'))
    
    return render_template('index.html', **user_data)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    message = None
    if request.method == 'POST':

        name = request.form.get('username')
        comment = request.form.get('user_comment')

        message = f'Thank you {name}! Your comment:\n{comment}\n was created'
        print(f'DEBUG: Form submitted - Name {name}, Comment: {comment}')
        context = {
            'name': name,
            'comment': comment,
            'message': message
        }
        return render_template('feedback_result.html', **context)

    return render_template('form.html', message=message)



# @app.route('/')
# def home_page():
#     return "Hello, I was created by Flask and Python!"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f"Hello {username}"

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f"Post ID: {post_id} (Type: {str(type(post_id))})"

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return f'Subpath: {subpath}'

if __name__ == '__main__':
    app.run(debug=True)