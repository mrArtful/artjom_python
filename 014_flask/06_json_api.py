from flask import Flask, jsonify

app = Flask(__name__)

# A simple list of dictionaries to simulate a database
users = [
    {"id": 1, "name": "Artjom", "role": "Student"},
    {"id": 2, "name": "Roman", "role": "Teacher"},
    {"id": 3, "name": "Gemini", "role": "Assistant"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    # jsonify() converts a Python list or dictionary into a JSON response.
    # It also sets the Content-Type header to 'application/json'.
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Find the user by ID
    user = next((u for u in users if u["id"] == user_id), None)
    
    if user:
        return jsonify(user)
    else:
        # Return a 404 error with a JSON message
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
