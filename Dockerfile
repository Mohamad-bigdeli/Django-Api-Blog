FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

RUN sed -i 's/http:\/\/[a-zA-Z0-9]*.[a-zA-Z0-9]*.*.com/http:\/\/ir.ubuntu.sindad.cloud/g' /etc/apt/sources.list

COPY requirements.txt /app/

RUN pip3 install --upgrade pip -i https://mirror-pypi.runflare.com/simple
RUN pip3 install -r requirements.txt 
COPY ./core /app/

CMD gunicorn -b 0.0.0.0:8000 core.wsgi --timeout 60

