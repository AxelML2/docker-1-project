FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements-app.txt .

RUN pip install -r requirements-app.txt

COPY app.py .

ENTRYPOINT python app.py