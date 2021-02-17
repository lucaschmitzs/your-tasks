FROM python:3.8

LABEL MAINTAINER="Lucas Schmitz <lucaschmitzsantos@gmail.com>"

COPY . /var/www
WORKDIR /var/www

RUN apt-get -y update
COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_APP=login_system
ENV FLASK_DEBUG=1
CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]