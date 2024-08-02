from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.db import db
from src.models.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"])
    new_user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        role=data["role"],
    )
    db.session.add(new_user)
    db.session.commit()
    return (
        jsonify(
            {
                "message": "User registered successfully!",
                "data": {
                    "user": {
                        "username": new_user.username,
                        "email": new_user.email,
                        "role": new_user.role,
                    },
                },
            }
        ),
        201,
    )


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and check_password_hash(user.password, data["password"]):
        return jsonify(
            {
                "message": "Login successful!",
                "data": {
                    "user": {
                        "username": user.username,
                        "email": user.email,
                        "role": user.role,
                    },
                },
            }
        )
    return jsonify({"message": "Invalid credentials"}), 401
