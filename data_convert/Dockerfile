FROM ubuntu

RUN apt-get update -y
RUN apt-get -y install sudo

# Install AWS CLI dependencies
RUN apt-get update && \
    apt-get install -y python3-pip groff && \
    pip3 install --upgrade awscli
RUN sudo apt install cron

RUN mkdir /app
COPY convert.sh /app/convert.sh
RUN chmod +x /app/convert.sh

COPY root /var/spool/cron/crontabs/root
RUN chmod 600 /var/spool/cron/crontabs/root

RUN mkdir -p /app/data

ENTRYPOINT ["/usr/sbin/cron","-l","2","-f"]