from flask import Flask, jsonify
from data import USERS

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "CI/CD Demo App is running"}

@app.route("/users")
def get_users():
    return jsonify(USERS)

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = next((u for u in USERS if u["id"] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
