# Project-5
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

