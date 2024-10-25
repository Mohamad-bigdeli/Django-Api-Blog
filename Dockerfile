FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

COPY ./core /app/

CMD gunicorn -b 0.0.0.0:8000 core.wsgi