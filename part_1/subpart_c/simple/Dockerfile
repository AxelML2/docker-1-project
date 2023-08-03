FROM python:3.9-slim

WORKDIR /usr/src/app

COPY ./simple/requirements-simple.txt .

RUN pip install -r requirements-simple.txt

COPY ./simple/script-simple.py .

ENTRYPOINT python sscript-simple.py