FROM python:3.8.5-alpine

ENV HOME=/home/app/
ENV APP_HOME=/home/app/voxy/

# Create directory for the app user
RUN mkdir -p $HOME $APP_HOME

# Create the app user
RUN addgroup -S app && adduser -S -G app app

WORKDIR $HOME
COPY Pipfile Pipfile.lock ./
COPY voxy ./voxy

# To make layers and help and make process agile, for production docker image should be '&&'
RUN chown -R app:app $HOME

RUN pip install --upgrade pip --no-cache-dir
RUN pip install pipenv --no-cache-dir
RUN pipenv install --system

COPY setup.py setup.cfg $HOME
RUN pip install .

EXPOSE 5000

#USER app
