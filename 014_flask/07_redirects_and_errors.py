from flask import Flask, redirect, url_for, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Home Page</h1><p>Visit /secret to see a redirect, or /missing to see a 404 error.</p>"

@app.route('/secret')
def secret():
    # redirect() sends the user to a different URL.
    # url_for() dynamically generates the URL for a function name.
    # This is better than hardcoding '/'.
    print("User tried to access /secret - Redirecting to home.")
    return redirect(url_for('home'))

@app.route('/user/<username>')
def profile(username):
    if username.lower() == 'admin':
        # abort() stops the request and returns an error code.
        abort(401) # 401 Unauthorized
    return f"Profile page of {username}"

# Custom error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    # We can return a custom template for errors
    return render_template('404.html'), 404

# Custom error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized(e):
    return "<h1>401 Unauthorized</h1><p>You are not allowed to see this page!</p>", 401

if __name__ == '__main__':
    app.run(debug=True)
