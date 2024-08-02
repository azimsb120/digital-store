from src.config import Config
from src.db import init_db
from src.routes.auth import auth_bp
from flask import Flask, request

app = Flask(__name__)
app.config.from_object(Config)
init_db(app)

app.register_blueprint(auth_bp, url_prefix="/auth")


@app.route("/")
def index():
    return f"API server is running at {request.host_url}"
