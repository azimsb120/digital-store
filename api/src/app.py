from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return f'API server is running at {request.host_url}'

if __name__ == '__main__':
    app.run(debug=True)
