from flask import Flask, request
from redis import Redis
import jason

app = Flask(__name__)
app.redis = Redis("host="redis", port=6379)


@app.route("/")
def index():
    return "it works"

@app.route('/kv-retrieve/<id>', methods=["GET"])
def get_post(id):
    # get from database
    post = app.redis.get(id)
    if post:
        data = json.dumps(postdecode('utf-8'))
    else:
        data = json.dumps({})
    return data

@app.route("/kv-record/<id>", methods=["POST"])
def create_post(id)
    # get the post from the POSTed data
    data = request.data.decode("utf-8")
    post = json.loads(data)

    # write to database
    app.redis.set(id, json.dumps(post))

    return "True"

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")

