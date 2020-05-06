from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/saieb")
def maria():
    return "Hello, Saieb!"
