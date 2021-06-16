# pull official base image
FROM python:3.9.1-slim-buster

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean



# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# install netcat
# Placing code at the end of file we prevent docker image from
# downloading stuff that was done in previos builds
RUN apt-get -y install netcat

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod 777 /usr/src/app/entrypoint.sh

# add app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
