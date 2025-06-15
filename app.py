from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.secret_key = 'your-secret-key'  # Required for session

# Dummy user list
USERS = {
    "john": "pass123",
    "alice": "alice123"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if USERS.get(username) == password:
        session['username'] = username
        return jsonify({"message": "Login successful"})
    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})

