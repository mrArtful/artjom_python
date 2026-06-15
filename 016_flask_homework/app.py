from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'notes.json'

def load_notes():
    """Helper function to load notes from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notes(notes):
    """Helper function to save notes to JSON file."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, indent=4)

@app.route('/')
def index():
    # TODO: Load notes and pass them to index.html
    return "Home Page"

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        # TODO: Get title and content from request.form
        # TODO: Create a new note dictionary with a unique ID and current timestamp
        # TODO: Load existing notes, append the new one, and save
        # TODO: Redirect to the index page
        pass
    
    # TODO: Render add_note.html for GET request
    return "Add Note Page"

@app.route('/note/<int:note_id>')
def note_detail(note_id):
    # TODO: Load notes and find the one with the matching note_id
    # TODO: Render note_detail.html with the note data
    # TODO: Handle the case where the note is not found (404)
    return f"Note {note_id} Detail"

if __name__ == '__main__':
    app.run(debug=True)
