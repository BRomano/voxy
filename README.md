# Voxy

[![ci](https://github.com/BRomano/voxy/actions/workflows/ci.yml/badge.svg)](https://github.com/BRomano/voxy/actions/workflows/ci.yml)

## 

As the test said we can just go on...
# 
1. For package manager I choose to use pipenv
2. Also I choose to create two applications, one for frontend using vue.js and another for backend in Python/Flask
3. For Backend I am using OpenAPI 3.0 (Swagger) to document every endpoint
4. Algo for helping to run the project I am putting the project inside a docker-compose
   1. So I created 2 inner projects front is the vue.js application and nginx for reverse proxy, and it will be build inside a container
   2. For backend the container will be created based on voxy/Dockerfile
5. To show a small knowledge with tests, I created some tests on tests folders using pytest, and a github action to run these tests with linter and coverage.
6. To run the whole project just need to pull the repository and docker-compose up

# Applications
## Front
1. Choosed to create two way to submit sentences, one by text input, and another to submit a text file (*.txt)
   1. Both of these methods will call a backend endpoint documented on OpenAPI
## Backend
1. Choose to create two endpoints, one to count words, and another to count each character on submitted sentence

> TODO ajustar: The code above will limit the maximum allowed payload to 16 megabytes. If a larger file is transmitted, Flask will raise a RequestEntityTooLarge exception.
> Allowed content-type
