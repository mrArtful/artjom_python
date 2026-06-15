from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # home.html extends layout.html
    return render_template('home.html')

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple demo of static files and template inheritance.</p>"

if __name__ == '__main__':
    app.run(debug=True)
