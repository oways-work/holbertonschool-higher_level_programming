#!/usr/bin/python3
"""
Task 5: API Security and Authentication Techniques
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuration for JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production
jwt = JWTManager(app)

# User data stored in memory
users = {
      "user1": {
                "username": "user1",
                "password": generate_password_hash("password"),
                "role": "user"
      },
      "admin1": {
                "username": "admin1",
                "password": generate_password_hash("password"),
                "role": "admin"
      }
}


@auth.verify_password
def verify_password(username, password):
      """
          Verifies the password for Basic Auth.
              """
      user = users.get(username)
      if user and check_password_hash(user['password'], password):
                return username
            return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
      """
          Route protected by Basic Auth.
              """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
      """
          Route to login and generate a JWT token.
              """
    data = request.get_json(silent=True)
    if not data:
              return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if user and check_password_hash(user['password'], password):
              # Create access token with username and role included in identity
              # or separate claims. Storing role in identity for simplicity here
              # is okay, or you can pass a dict.
              access_token = create_access_token(identity={
                            "username": username,
                            "role": user["role"]
              })
              return jsonify(access_token=access_token)

    return jsonify({"error": "Bad username or password"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
      """
          Route protected by JWT Auth.
              """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
      """
          Route accessible only to admins.
              """
    current_user = get_jwt_identity()

    # get_jwt_identity returns the object we passed to create_access_token
    if current_user['role'] != 'admin':
              return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# --- Custom JWT Error Handlers (Required for Task) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
      return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
      return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
      return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
      return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
      return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
      app.run()
