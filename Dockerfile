FROM python:3.6


WORKDIR /home/user

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY appfolder appfolder
COPY migrations migrations
COPY microblog.py microblog.py
COPY config.py config.py
COPY boot.sh boot.sh

ENV http_proxy host:port
ENV https_proxy host:port

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]

