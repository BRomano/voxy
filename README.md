# Voxy

[![ci](https://github.com/BRomano/voxy/actions/workflows/ci.yml/badge.svg)](https://github.com/BRomano/voxy/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/BRomano/voxy/branch/main/graph/badge.svg?token=LQ84XHL1O3)](https://codecov.io/gh/BRomano/voxy)

## 
> The application is Running on [this IP](http://159.223.180.98) check it if you want.

> To run the test, just git pull && docker-compose up

## Some decision on implementations
1. For package manager I choose to use pipenv, it is integrated on Docker build, and on a small CI process;
2. Also I choose to create two applications, one for frontend using vue.js and another for backend in Python/Flask;
3. For Backend I am using OpenAPI 3.0 (Swagger) to document every [endpoint](http://159.223.180.98/api/apidocs/);
4. Algo for helping to run the project I am putting the project inside a [docker-compose](https://github.com/BRomano/voxy/blob/main/docker-compose.yml)
   1. So I created 2 inner projects one for frontend with vue.js, tailwind and nginx for reverse proxy.
   2. For backend the container will be created based on voxy/Dockerfile, and run inside a gunicorn, it will run 4 instances, it is all configured on docker-compose yml;
5. To show a small knowledge with tests, I created some tests on tests folders using pytest
   1. And a github action CI to run these tests with linter and coverage.
6. To run the whole project just need to pull the repository and run docker-compose up, docker-compose need to be installed.
   1. Or you can access the application in [this link](http://159.223.180.98)

# Applications
## Front
1. Choosed to create two way to submit sentences, one by text input, and another to submit a text file (*.txt)
   1. If you just write some words on textarea and submit, it will count only words, not pontuations.
   2. If you choose to submit a file, frontend will load the first 200 characters and show on textarea, but will submit the whole file to backend;
   3. The frontend are using [tailwind.css](https://tailwindcss.com/), typescript and vue.js
   4. 
## Backend
1. I choosed to create two endpoints
   1. One to count words on a sentence
   2. Another to count words on a text file
2. Both endpoints are documented by [openApi](http://159.223.180.98/api/apidocs/)
   1. And can be tested by API.
3. The Coverage can be seen on this [link](https://app.codecov.io/gh/BRomano/voxy)
4. For security and enviroments I have configured MAX_CONTENT_LENGTH
5. The application on backend was builded as a package so it can scale horizontally, acordly to framework's [documentation](https://flask.palletsprojects.com/en/2.1.x/patterns/packages/)
6. The application is using multiple routes, and is started as a [module](https://github.com/BRomano/voxy/blob/main/voxy/__init__.py);
7. And for better management on multiple enviroments the application has a [config.py](https://github.com/BRomano/voxy/blob/main/voxy/config.py) so it can have multiple configurations for test, stagging, deployment;
   1. It can be seen when gunicorn is run, and on create_app() like "voxy:create_app('DevConfig')"

