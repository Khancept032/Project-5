import request, json
from flask import Flask, jsonify
from redis import Redis

app = Flask(__name__)

# Index Route
@app.route("/")
def index():
    return "Hello world!"

# Test Route
@app.route("/banana")
def banana_handler():
    return jsonify(
            output = "yes, is a banana again"
            )

# Record Route
# @app.route("/kv-record/<string:key>")
# def record(key):
#     data = request.data.decode("utf-8")
#     post = json.loads(data)

#     app.redis.set(key, json.dumps(post))

#     return "True"

# Record Route Version 2
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
		else:''
			raise

	except Exception as error:
		return json.dumps({"output": False, "error": str(error)})

# Retrieve Route
@app.route('/kv-retrieve/<string:key>')
def retrieve(key):
    try:
        if redis.exists(key):
                return json.dumps({"input": "retrieve-value", "output": redis.get(key)})
        else:
                return json.dumps({"input": "retrieve-value", "output": False, "error": "Not able to update value, the key does not exist."})

    except Exception as error:
        return json.dumps({"output": False, "error": str(error)})

# fibonacci Route
@app.route('/fibonacci/<fnumraw>')
def fibonacci(fnumraw):

    fold = 0
    fnew = 1
    fplaceholder = 0
    fnum = 0
    farray = []
    strfarray = ''

    #fnumraw = input("Give me a num ")

    if fnumraw.isdigit():
        fnum = int(fnumraw)
        fplaceholder = fnew + fold

        if fold < fnum:
            farray.append(fold)

        if fnew < fnum:
            farray.append(fnew)


        while fplaceholder <= fnum:
            farray.append(fplaceholder)
            fold = fnew
            fnew = fplaceholder
            fplaceholder = fnew + fold

        #strfarray = ' '.join(str(e) for e in farray)

        return jsonify (
            input = fnumraw,

            output = farray
            )

    else:
        return jsonify ("You must input a positive integer")


#md5 route

@app.route('/md5/<text>')
def md5(text):

    import hashlib
    from hashlib import md5

    outputtext = text
    textUtf8 = text.encode("utf-8")


    hash = hashlib.md5( textUtf8 )
    hexa = hash.hexdigest()

    #m = hashlib.md5()
    #m.update(text.encode('utf-8'))
    #md5string=m.digest()

    return jsonify (
        input = outputtext,
        output = hexa
        )


# is_prime route
@app.route('/is-prime/<num>')
def isprime(num):

    if num.isdigit():

        x=True
        inum = num
        num = int(num)

        for i in range(2, num//2):
            if(num % i) == 0:
                x = False
                break

        if num == 4:
            x = False

        if x:
            return jsonify (
                input = inum,
                output = True
            )

        else:
            return jsonify (
                input = inum,
                output = False
            )

    else:
        return jsonify ("You must input a positive integer")


#factorial route

@app.route('/factorial/<fnum>')
def factorial(fnum):

    ifnum = fnum

    if fnum == "0":
        return jsonify (
                input = ifnum,
                output = 1
            )

    elif fnum.isdigit():

        fnum = int(fnum)
        x = 1
        sfnum = fnum

        while x < fnum:
            sfnum = sfnum * x
            x = x + 1

        #sfnum = str(sfnum)

        return jsonify (
                input = ifnum,
                output = sfnum
            )
    else:
        return jsonify ("You must input a positive integer")


# slack-alert route
@app.route('/send_slack/<string:x>')
def send_slack(x):

    #print("Input: ", x)

    #change the url depending on the channel you want to post to
    web_hook_url = 'https://hooks.slack.com/services/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'

    #x = 6
    slack_msg = {'text':x}
    requests.post(web_hook_url,data=json.dumps(slack_msg))
    return jsonify(
        input=x,
        output=True
    )

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0", port=5000)

# a test change #6
