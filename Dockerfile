FROM python:2.7.9

ADD . /app

WORKDIR /app

RUN python2 setup.py develop
