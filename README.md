# Voxy

[![ci](https://github.com/BRomano/voxy/actions/workflows/ci.yml/badge.svg)](https://github.com/BRomano/voxy/actions/workflows/ci.yml)

## 

As the test said we can just go on...
# 
1. For package manager I choose to use pipenv, it is integrated on Docker build, and on a small CI process;
2. Also I choose to create two applications, one for frontend using vue.js and another for backend in Python/Flask;
3. For Backend I am using OpenAPI 3.0 (Swagger) to document every [endpoint](http://159.223.180.98/api/apidocs/);
4. Algo for helping to run the project I am putting the project inside a docker-compose
   1. So I created 2 inner projects one for frontend with vue.js, tailwind and nginx for reverse proxy.
   2. For backend the container will be created based on voxy/Dockerfile, and run inside a gunicorn, it will run 4 instances;
      1. Also the application has a [config.py]() file to manage enviroment variables and .env; 
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
1. Choose to create two endpoints
   1. One to count words on a sentence
   2. Another to count words on a text file
2. Both endpoints are documented by [openApi](http://159.223.180.98/api/apidocs/)

> TODO ajustar: The code above will limit the maximum allowed payload to 16 megabytes. If a larger file is transmitted, Flask will raise a RequestEntityTooLarge exception.
> Allowed content-type
