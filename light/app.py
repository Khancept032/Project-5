import flask, requests, json
from flask import Flask, jsonify

# DEMO CODE FROM LUKE: commented out for simplicity during setup
# from redis import Redis
# import json

app = Flask(__name__)

# DEMO CODE FROM LUKE: commented out for simplicity during setup
#app.redis = Redis("host="redis", port=6379)

# Index Route
@app.route("/")
def index():
    return "Hello world! \n I retrieve things!"


@app.route("/banana")
def banana_handler():
    return "this is a banana"


if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
