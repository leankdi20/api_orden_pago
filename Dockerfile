# Usa la imagen oficial de Python como base
FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update


COPY ./requirements.txt /requirements.txt
#RUN pip install python-dateutil celery
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN mkdir /app
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN adduser --disabled-password --no-create-home django-user

ENV PATH="py/bin:$PATH"

