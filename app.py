from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/hii')
def hii():
    return 'hello'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)