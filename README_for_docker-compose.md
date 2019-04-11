## FYI
The file in this directory called "docker-compose.yml" will make two containers, one called "heavy" that has all of our code except for /kv-retrieve/, and "light" that only has /kv-retrieve/. The goal of this part of the project is to make the light container talk to the heavy container.

*Heavy will be on http://localhost:5001 and Light will be on http://localhost:5002*

## Use
1. Navigate to the directory this "README_for_docker-compose" file is in
2. Run `docker-compose up`

## To make changes
1. `ctrl+c` to shut down containers
2. `docker-compose rm` and 'y' to clean up
3. 'docker rmi project-5_light project-5_heavy'
3. make changes to files and save
4. 'docker-compose up'

I am working on getting the containers to rebuild automatically when a change is detected, but I haven't got it working yet.
