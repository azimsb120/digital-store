from config import Config
from db import init_db
from flask import Flask, request

app = Flask(__name__)
app.config.from_object(Config)
init_db(app)


@app.route("/")
def index():
    return f"API server is running at {request.host_url}"


if __name__ == "__main__":
    app.run(debug=True)
