# Dockerfile
FROM python:3.10


RUN mkdir /bookstore
RUN mkdir /static


WORKDIR /bookstore

RUN apt-get update && apt-get install -y gettext libgettextpo-dev zlib1g libjpeg-dev


ENV PYTHONUNBUFFERED=1
RUN python3 -m pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt
#RUN python -m pip install uwsgi
COPY . /bookstore/

# Copy the wait-for-it script
COPY ./wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

ENV PYTHONPATH=/bookstore/bookstore

COPY docker-entrypoint.sh /bookstore/
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
