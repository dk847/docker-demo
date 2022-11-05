# Pull base image
FROM python:3.8.10

# Set env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME ./app

# Setup project
WORKDIR $APP_HOME
COPY dev.env $APP_HOME/.env
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN apt update && apt install -y && pip install -r $APP_HOME/requirements.txt

COPY . $APP_HOME
