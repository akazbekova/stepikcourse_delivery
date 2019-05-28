from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"

@app.route("/alive")
def alive():
    return '{"alive":true}'

@app.route("/workhours")
def workhours():
    return '{"opens":"10:00", "closes":"20:00"}'


app.run("localhost", 8000)