import flask, request
from flask import Flask, jsonify
import redis



app = Flask(__name__)



# Index Route
@app.route("/")
def index():
    return "Hello world! \n I retrieve things!"


@app.route("/banana")
def banana_handler():
    return jsonify(
            output = "yes, is a banana"
            )

# Retrieve Route
@app.route('/kv-retrieve/<string:key>')
def retrieve(key):
    try:
<<<<<<< HEAD
        if redis.exists(key):
=======
        if redis.exits(key):
>>>>>>> parent of e265a1a... update app.py
                return json.dumps({"input": "retrieve-value", "output": redis.get(key)})
        else:
                return json.dumps({"input": "retrieve-value", "output": False, "error": "Not able to update value, the key does not exist."})

    except Exception as error:
        return json.dumps({"output": False, "error": str(error)})



if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
