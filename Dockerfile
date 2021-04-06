From ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip

RUN pip install flask

COPY app.py  /opt/
EXPOSE 5000

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0