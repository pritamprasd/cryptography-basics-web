FROM ubuntu:20.04

WORKDIR /app

RUN apt update
# RUN apt-get install -y software-properties-common gcc
RUN apt install python3 -y
RUN apt install pip -y
RUN pip install pip --upgrade

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 5000