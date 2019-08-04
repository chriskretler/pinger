FROM python:3.7

MAINTAINER Chris Kretler <ckretler@umich.edu>

RUN apt-get update \
	&& apt-get install -y curl net-tools dnsutils

WORKDIR /app/

COPY *.py /app/

#CMD ["/bin/bash"]
CMD ["tail", "-f", "/dev/null"]
#CMD ["python", "pinger.py"]
#CMD ["python", "dns.py"]
