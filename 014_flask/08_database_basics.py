import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

DB_NAME = 'database.db'

def init_db():
    """Create the table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    """Helper to get a connection to the database."""
    conn = sqlite3.connect(DB_NAME)
    # This allows us to access columns by name (like a dictionary)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # Fetch all messages from the database
    messages = conn.execute('SELECT * FROM messages ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('db_index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    name = request.form['name']
    content = request.form['content']
    
    if name and content:
        conn = get_db_connection()
        conn.execute('INSERT INTO messages (name, content) VALUES (?, ?)', (name, content))
        conn.commit()
        conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
