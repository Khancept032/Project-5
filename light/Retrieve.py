#Using this file to do some testing for retrieve

from flask import flask, request, jsonify
from redis import Redis
import json


app = Flask(__name__)


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
