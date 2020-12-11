## Notes on a Udemy course
https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide

## Install docker

## Docker image

Nothing else than:
 - file snapshot
 - startup command

Container = file snapshot + separated area of HW on the machine = own piece of disk, networking etc. 

## Run docker images

### Start a second process in image
 - `docker ps` - to get the <image_id> 
 - `docker exec -it <image_id> sh`

### Port mapping
 - container can make outgoing requests by default = it can download packages from the internet
 - inbound requests MUST be propagated through port mapping = 
   - map local machine port to some port inside the container
   - `docker run -p <local_port>:<container_port> <image_id>`

## Build Dockerfile

### Dockerfile
 - FROM <base_image>
 - RUN instruction installing additional software using programs from base image = like apt-get, ...
 - RUN another instruction installing / downloading something else
 - RUN ...
 - WORKDIR <dir_path_in_container> = e.g. `WORKDIR /usr/app` => all following commands will be done inside this dir
 - COPY `<relative_local_path>` `<path_in_container>` = e.g. `COPY ./ ./` => will be copied to `/usr/app/`
 - CMD ["startup_command"]

### Building
 - docker build -t `<your_docker_id>/<project_name>:<version>` <directory>
   - calls `docker client` -> `docker server` -> generates usable image
   - -t tags = names the image

For each instruction in the Dockerfile do:
 1. create a temporary container TC = use a file system snapshot from the previous step
 2. execute the one instruction in the TC = e.g. installs some packages
 3. take a snapshot of the file system of this TC
 4. create a new temporary container with this file snapshot = step 1.
 5. after the last instruction is run, take a file system snapshot of the container and save it 
    with the startup command as the newly built image 

### Caching
 - rebuilding uses cache for each step described above 
 - BUT all the instructions after a changed instruction WILL be rerun, not taken from cache
 - => always COPY only the necessary files for the next steps such as installing dependencies and COPY the rest of the files at the last instruction so if we rebuild the image we will not have to rerun the dependency installation steps


## Networking between docker containers
Either:
 - use Docker CLI: too complicated
 - use Docker Compose

### Docker compose
 - separate CLI tool installed with docker
 - wrapper around docker CLI
 - used to start multiple containers at once
 - automatically connect them together with some networking

#### Docker Compose Usage
 - docker-compose.yaml
   - automatically creates the containers in the same network 
     = no need explicitly to open up their ports
   - create containers
   - map their ports to outside = local machine

```
version: '3'
services:
  my-redis-server:
    image: 'redis'   = just use image called redis
  my-node-app:
    build: 
      context: .         = build image in local dir
      dockerfile: Dockerfile.dev   = specify if diff name than Dockerfile
    ports:
      - "4001:8081"  = local machine port:in_container port 
    volumes:
      - /app/node_modules  = do not map /app/node_modules
      - .:/app       = pwd -> /app in container
```

 - instead of host URL use: `my-redis-server` to get into the redis container 
   from the `my-node-app` container
 
#### Docker Compose CLI Usage
 - `docker-compose up` = start all services defined in the local yaml
 - `docker-compose up -d` = start in background
 - `docker-compose up --build` = rebuild
 - `docker-compose down` = stop all services
 - `docker-compose ps` = get status of running containers from the local yml

#### Automatic container restarts with Docker Compose
 - restart policy in docker-compose file
   - "no" = has to be in quotes because yaml has `no` as a keyword
   - always
   - on-failure = checks exit code
   - unless-stopped = unless we manually stop it from CLI

## Development + Deployment flow
 - github repo
 - MR
 - Travis CI runs tests and merges to master runs tests again and pushes to AWS
 - AWS instance

### Docker images
Different for dev and prod =>
 - `Dockerfile.dev` = used for dev = e.g. start dev Flask server isntead of running Gunicorn
   - `docker buils -f Dockerfile.dev .`
 - `Dockerfile` = used for production

### Docker volumes
 - propagate changes in source code files into the container without rebuilding the container
 - do not COPY files but create references in the container pointing to the files outside the container
 - `docker run -v /app/node_modules -v $(pwd):/app <image>` 
   - `-v $(pwd):/app` will map pwd to `/app` inside the container
   - `-v /app/node_modules` will say: do not touch `/app/node_modules` inside the container = do not map it
   - without last command the `/app/node_modules` inside comtainer would be mapped to an empty space because we don't have that folder in current working dir (we installed the node_modules to another dir)
   - => do not map folders where the container installs stuff

### Running tests and interacting with them
 - add tests service to docker compose, that will have the volumes mounted but changed the starting command
 - docker attach always attaches to the primary process of a container = with pid=1
   - if the primary process starts a secondary process we cannot attach to it = cannot pass input to it

 - or run tests in the main container using `docker exec -it run tests`

### Multi-step Docker builds
 - Build phase:
   - uses node:alpine 
   - istall node dependencies
   - run npm run build = outputs build directory with static files
 - Run phase:
   - uses nginx image
   - copy over results of the build phase
   - start nginx

```
FROM node:alpine
WORKDIR '/app'
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx
COPY --from=0 /app/build /usr/share/nginx/html            = from=0 = from phase 0
```

### Travis CI
 - amytime we push to github, travis will pull the code and do some work = testing, deploying
 - `.travis.yaml` in project root:
   - sudo: required = needed for docker
   - install docker:
     - services:
       - docker
   - build our image from Dockerfile.dev
     - before_install:
       - docker build -t travis-test-image -f Dockerfile.dev .
   - run the test suite, travis expects that every command runs and exits with return code 0, if not it failed
     - script:
       - docker run travis-test-image <run_tests>
   - if tests pass, deploy to AWS Elastic Beanstalk
     - deploy:
       - fill in info about elastic beanstalk
       - on:
         - branch: master
     - access keys to aws = create a new AMI user with Beanstalk full access right

 - add environment variables to our project in Travis
   - acessKey, secretKey for AWS - display value in log = FALSE

### AWS Elastic Beanstalk
 - sets up: 
   - Load Balancer 
   - S3 bucket
   - and a VM running our docker container
 - automatically scales up = starts new VM running our docker image

 - automatically maps ports to outside that are specified by: `EXPOSE: 80` in the dockerfile
   - this is specific feature of the AWS Elastic Beanstalk
   - the Dockerfile then looks like this:
```
FROM node:alpine
WORKDIR '/app'
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx
EXPOSE 80
COPY --from=0 /app/build /usr/share/nginx/html
```
