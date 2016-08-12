FROM ubuntu:16.04

MAINTAINER Chris Kretler <ckretler@umich.edu>

RUN apt-get update \
#	&& apt-get install -y vim python python-pip git
	&& apt-get install -y python python-pip

# create place for app to run from
WORKDIR /app/

COPY . /app/

#RUN pip install -r requirements.txt

CMD ["python", "pinger.py"]