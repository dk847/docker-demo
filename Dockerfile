# Pull base image
FROM python:3.8.10

# Set env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME ./app

# Create/add user "app" and copy project
RUN addgroup app && useradd app -g app
WORKDIR $APP_HOME

# Copy .env file
COPY dev.env $APP_HOME/.env

# Copy and install requirements.txt
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN apt update && apt install -y && pip install -r $APP_HOME/requirements.txt

# Copy project
COPY . $APP_HOME

# Set permissions, change to user and collect static files
RUN chown -R app:app $APP_HOME
USER app
RUN cd $APP_HOME
