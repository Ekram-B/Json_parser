FROM ubuntu:latest
MAINTAINER Ekram Bhuiyan "ekram67@my.yorku.ca"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install flask
RUN apt-get install -y firefox
RUN apt-get clean

RUN groupadd --gid 1000 user && \
        useradd --uid 1000 --gid 1000 --create-home user

RUN usermod -aG sudo user
RUN export DISPLAY=:1
ENV HOME /home/user
 
CMD /usr/bin/firefox


RUN apt-get install zip -y
RUN apt-get install gedit -y

COPY ./Deeplearni_ng.zip /usr/local/Deeplearni_ng/
