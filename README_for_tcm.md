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
