FROM ubuntu

RUN apt-get update -y
RUN apt-get -y install sudo

# Install AWS CLI dependencies
RUN apt-get update && \
    apt-get install -y python3-pip groff python3 && \
    pip3 install --upgrade awscli && \
    pip3 install pandas
RUN sudo apt install cron

RUN mkdir /app
COPY convert.sh /app/convert.sh
RUN chmod +x /app/convert.sh
COPY data_convert.py /app/data_convert.py
RUN chmod +x /app/data_convert.py

COPY root /var/spool/cron/crontabs/root
RUN chmod 600 /var/spool/cron/crontabs/root

RUN mkdir -p /app/data

ENTRYPOINT ["/usr/sbin/cron","-l","2","-f"]