from src.config import Config
from src.db import init_db
from flask import Flask, request

app = Flask(__name__)
app.config.from_object(Config)
init_db(app)


@app.route("/")
def index():
    return f"API server is running at {request.host_url}"
