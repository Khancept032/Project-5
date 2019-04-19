import flask, requests, json
from flask import Flask, jsonify
import redis

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

@app.route('/kv-retrieve/<string:key>')
def retrieve(key):
    try;
        if redis.exits(key):
                return json.dumps({"input": "retrieve-value", "output": redis.get(key)})
        else:
                return json.dumps({"input": "retrieve-value", "output" False, "error": "Not able to update value, the key does not exist."})

    except Exception as error:
        return json.dumps({"output": False, "error": str(error)})



if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
