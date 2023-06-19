# Docker
docker run --name starlette_web_fe_be -it -p 5002:8000 -v ${PWD}/app:/app:rw python:3.10.6-slim-bullseye /bin/bash
https://gitlab.com/q347/gpt3_trans.git

docker build -t registry.gitlab.com/trongbach/starlette_web_demo/web_be_fe:v0.1 .
docker run --name starlette_demo -it -p 5002:8000 -v ${PWD}/app:/app:rw registry.gitlab.com/trongbach/starlette_web_demo/web_be_fe:v0.1 /bin/bash
docker push registry.gitlab.com/trongbach/starlette_web_demo/web_be_fe:v0.1

# Run test
## In docker
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
## Local
docker-compose -f docker-compose_test.yml up
