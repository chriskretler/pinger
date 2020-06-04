FROM python:3.8

MAINTAINER Chris Kretler <ckretler@umich.edu>

RUN apt-get update \
	&& apt-get install -y curl net-tools dnsutils traceroute

ADD requirements .
RUN pip install -r requirements

WORKDIR /app/
COPY /src .
RUN chmod +x start.sh

ENV SITES https://google.com

CMD ["./start.sh"]
