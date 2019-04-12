# Outdated, see README_for_docker-compose

## Setting Up for Project-5
1. Clone `https://github.com/Khancept032/Project-5` somewhere
2. Go into the freshly cloned repo
3. Run `docker login` to make sure you are logged in
4. Run `docker pull nathanhtaylor/p5` to pull docker image
5. Run `docker build --tag=p5 .` to set up docker image
6. Run `docker run -ti --rm -p 5000:5000 p5`
7. Open `http://localhost:5000` or `http://0.0.0.0:5000` in browser


## Coding for Project-5
Steps 5-7 must be repeated every time a change to code is made. This includes fetching from origin and code that you write and want to test.


## Project-5
Extend and publish your API

PART 1: Extend the API

You will add two new endpoints to your API, whose purpose is to record and retrieve pairs of key-value variables. You should store this data in a Redis database that is running in a separate container from your API: this means that these two containers will need to communicate with each other in order for your Flask app to store and retrieve data from Redis.

/kv-record/

This endpoint will record the value POSTed to the URI and save it in the datastore attached to the key supplied in the URL. The only HTTP methods methods this URL should accept are POST (to create a new key-value pair) and PUT (to update the value on an existing key). The output payload should return a boolean that indicates success, and if false , the error payload should include a message that indicates why the creation or update failed.

/kv-retrieve/

This endpoint will retrieve the value associated with the key supplied in the URL. The output will contain the value if successful, or false if unsuccessful. If the output is false, the error payload should contain a message that indicates why retrieval failed.

You should return a JSON payload with three values. For example, the /kv-record/new-key endpoint might return this payload:

{
    "input": "new-key",
    "output": false,
    "error": "Unable to add pair: key already exists."

}
