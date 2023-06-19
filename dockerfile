FROM tiangolo/uvicorn-gunicorn-starlette:python3.11-slim

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install -r requirements.txt

RUN pip install parsel
