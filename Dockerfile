FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1


RUN mkdir /app
COPY . /app
WORKDIR /app
 
RUN pip install --upgrade pip

# Installing dependencies for building 
RUN apk update \
    && apk add ffmpeg
 

COPY ./requirements.txt /backend/

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /

