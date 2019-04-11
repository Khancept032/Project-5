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
    return "Hello world!"



@app.route("/banana")
def banana_handler():
    return jsonify(
            isbanana = "yes, is a banana"
            )



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

        strfarray = ' '.join(str(e) for e in farray)
        return strfarray

    else:
        return "You must input a positive integer"



# md5 Route
@app.route('/md5/<text>')
def md5s(text):

    import hashlib
    from hashlib import md5

    textUtf8 = text.encode("utf-8")

    hash = hashlib.md5( textUtf8 )
    hexa = hash.hexdigest()

    #m = hashlib.md5()
    #m.update(text.encode('utf-8'))
    #md5string=m.digest()

    return hexa



# is_prime route
@app.route('/is_prime/<int:num>')
def is_prime(num):
    num = int(num)
    if num < 2:
        result = "Enter number larger than 1"
        return jsonify(
            input=num,
            output=result
        )
    else:
        for x in range(2,num):
            if num % x == 0:
                result = "Not a prime"
                return jsonify(
                   input=num,
                   output=result
                )
        result = "Is a prime"
        return jsonify(
            input=num,
            output=result
        )



#factorial route
@app.route('/factorial/<fnum>')
def factorial(fnum):
    if fnum == "0":
        return "1"

    elif fnum.isdigit():
        fnum = int(fnum)
        x = 1
        sfnum = fnum
        while x < fnum:
            sfnum = sfnum * x
            x = x + 1
        sfnum = str(sfnum)
        return sfnum
    else:
        return "You must input a positive integer"



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



# DEMO CODE FROM LUKE: commented out for simplicity during setup
# @app.route('/kv-retrieve/<id>', methods=["GET"])
# def get_post(id):
#     # get from database
#     post = app.redis.get(id)
#     if post:
#         data = json.dumps(postdecode('utf-8'))
#     else:
#         data = json.dumps({})
#     return data
#
# @app.route("/kv-record/<id>", methods=["POST"])
# def create_post(id)
#     # get the post from the POSTed data
#     data = request.data.decode("utf-8")
#     post = json.loads(data)
#
#     # write to database
#     app.redis.set(id, json.dumps(post))
#
#     return "True"



if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0", port=5000)
