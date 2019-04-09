#Using this file to do some testing for retrieve

from flask import flask, request
from redis import Redis
import json

app = Flask(__name__)
app.redis = Redis(host="redis", port=6379)

@app.route('/kv-retrieve/<id>', methods=["GET"])












if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
