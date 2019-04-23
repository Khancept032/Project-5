## FYI
The file in this directory called "docker-compose.yml" will make two containers, one called "heavy" that has all of our code except for /kv-retrieve/, and "light" that only has /kv-retrieve/. The goal of this part of the project is to make the light container talk to the heavy container.

## Veiwing API
### Docker Desktop:
1. Follow steps in *Use*
2. *Heavy will be on http://localhost:5001 and Light will be on http://localhost:5002*

### Docker Toolbox:
1. Follow steps in *Use*
2. run `docker-machine ip`
3. take IP addess from step 2 and plug it in to browser followed by port 5001 or 5002. e.g.: *http://xxx.xxx.xxx.xxx:5001 for heavy and http://xxx.xxx.xxx.xxx:5002 for light*


## Use
1. Navigate to the directory this "README_for_docker-compose" file is in
2. Run `docker-compose up -d`

## To make changes
1. `docker-compose down` to shut down containers
2. make changes to files and save
3. 'docker-compose build'
4. 'docker-compose up'

I am working on getting the containers to rebuild automatically when a change is detected, but I haven't got it working yet.