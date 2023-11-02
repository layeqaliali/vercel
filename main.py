from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Vercel App"


@app.route("/about")
def about():
    return "Hello World"