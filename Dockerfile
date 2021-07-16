# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
EXPOSE 5000/tcp

ENV PYTHONPATH "${PYTHONPATH}:/var/www/test"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /var/www/test/
WORKDIR /var/www/test

RUN pip install -r requirements.txt
