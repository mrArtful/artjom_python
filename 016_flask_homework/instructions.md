# Homework: Flask Personal Note-Taking App

In this homework, you will build a simple web application to manage your personal notes. 
You will use everything we've learned so far: Flask routes, template inheritance, form handling, and JSON data persistence.

## Task Overview

Build a Flask application that allows a user to:
1.  **View all notes** on the homepage.
2.  **Add a new note** via a web form.
3.  **View details** of a specific note.
4.  **Persist data** in a `notes.json` file.

## Requirements

### 1. Project Structure
Your project should follow this structure:
```text
016_flask_homework/
├── app.py              # Main Flask application
├── notes.json          # Data storage (created automatically or manually)
├── static/
│   └── style.css       # Your custom CSS
└── templates/
    ├── base.html       # Base template with layout
    ├── index.html      # Home page (list of notes)
    ├── add_note.html   # Form to add a new note
    └── note_detail.html # Page to view a single note
```

### 2. The Data (notes.json)
Each note should be a dictionary with at least these fields:
- `id`: A unique integer.
- `title`: String.
- `content`: String.
- `date`: String (current date/time).

Example:
```json
[
    {
        "id": 1,
        "title": "Learn Flask",
        "content": "Today I learned about routes and templates.",
        "date": "2026-06-15 14:00"
    }
]
```

### 3. Routes to Implement
- `GET /`: Show all notes titles as links to their detail pages.
- `GET /add`: Show a form with inputs for "Title" and "Content".
- `POST /add`: Process the form data, add a new note to `notes.json`, and redirect to `/`.
- `GET /note/<int:note_id>`: Show the full title, date, and content of a specific note.

### 4. Templates
- **base.html**: Should contain the `<html>` structure, link to `style.css`, and a navigation bar (links to "Home" and "Add Note").
- **index.html**: Extends `base.html`, loops through notes and displays them.
- **add_note.html**: Extends `base.html`, contains the `<form>`.
- **note_detail.html**: Extends `base.html`, shows the details of one note.

### 5. Bonus (Optional)
- Add a "Delete" button for each note.
- Sort notes so the newest ones appear at the top.
- Add some nice CSS styling to make it look like a real notebook.

---
**Good luck!**
