import flask, requests, json
from flask import Flask, jsonify
import redis

app = Flask(__name__)

@app.route('/kv-record/<string:key>', methods = ["POST", "PUT"])
def record(key):
	try:
		data = request.get_json(force=True)
		value = data['value']
		key = data['key']
		if request.method == "POST":
			if redis.exists(key):
				return json.dumps({"input": "new-key", "output": False, "error": "Not able to add pair: the key already exists."})
			else:
				redis.set(key, value)
				return json.dumps({"input": "new-key", "output": True})

		elif request.method == "PUT":
			if redis.exists(key):
				redis.set(key, value)
				return json.dumps({"input": "existing-key", "output": True})
			else:
				return json.dumps({"input": "existing-key", "output": False, "error": "Not able to update value: the key does not exist."})
		else:
			raise
			
	except Exception as error:
		return json.dumps({"output": False, "error": str(error)})



if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0", port=5000)