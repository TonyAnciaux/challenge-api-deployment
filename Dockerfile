FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common gcc && \
    add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.8 python3-distutils python3-pip python3-apt

RUN mkdir /app

copy . /app

WORKDIR /app

RUN rm -rf venv


RUN pip3 install -r requirements.txt

CMD python3 app.py 