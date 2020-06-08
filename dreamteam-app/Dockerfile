FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y  python-dev build-essential libmysqlclient-dev gcc libssl-dev

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["/usr/local/bin/flask", "db", "init"]
CMD ["/usr/local/bin/flask", "db", "migrate"]
CMD ["/usr/local/bin/flask", "db", "upgrade"]
CMD ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
