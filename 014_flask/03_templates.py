from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # render_template looks for files in the 'templates' folder.
    # We can pass variables to the template as keyword arguments.
    user_data = {
        'name': 'Artjom',
        'title': 'My Flask App',
        'items': ['Learn Python', 'Learn Flask', 'Build a Website']
    }
    
    return render_template('index.html', **user_data)

@app.route('/empty')
def empty_list():
    return render_template('index.html', name='Guest', title='Empty List', items=[])

if __name__ == '__main__':
    app.run(debug=True)
