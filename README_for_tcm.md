## Using the tcm.py CLI
`tcm.py` is a command line interface (CLI) for project 5 of Texas Chainsaw Managers. Using the syntax `python tcm.py [endpoint] [arguement]` the CLI will communicate with Flask-powered REST APIs running on localhost. These containers are powered by Docker and are created with a Docker compose file.

### System Requirements:
The system running tcm.py must have:
1. **Docker**, for creating Docker containers
2. **Python**
3. the python library **docopt**
4. the python library **requests**

### Using this CLI
1. Run `docker-compose up -d` while in the same directory as `docker-compose.yml`
2. Begin running commands with the `python tcm.py [endpoint] [arguement]` syntax.

For example: `python tcm.py banana` will call the endpoint `http://localhost:5000/banana` from the REST API and return its contents.

### CLI commands
* banana
  * A test endpoint that the code monkeys forgot to remove
* is-prime <input>
  * Returns `True` if input is a prime number, otherwise returns `False`
* md5 <input>...
  * Creates an md5 hash out of the input
* fibonacci <input>
  * Gives a list of the fibonacci numbers less than the input
* factorial <input>
  * Makes a factorial of the input by multiplying it by all of its preceding integers
* slack-alert <input>...
  * Sends a message to the Texas Chainsaw Managers' botspam channel in the Slack workspace tcmg476sp19.slack.com
* kv-record <input>
  * Records the input as a redis key value (via API named "heavy")
* kv-retrieve <input>
  * Retrieves any redis key value that is the input (via API named "light")
