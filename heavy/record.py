from flask import flask, request, jsonify
from redis import Redis
import json

app = Flask(__name__)

@app.route("/kv-record/<string:key>")
def record(key):
    data = request.data.decode("utf-8")
    post = json.loads(data)

    app.redis.set(key, json.dumps(post))

    return "True"
    
if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
