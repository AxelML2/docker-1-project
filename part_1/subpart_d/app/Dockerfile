FROM python:3.9-slim

WORKDIR /usr/src/app

# copy whole app while being inside the folder (Dockerfile in this folder)
COPY app.py . 
COPY requirements.txt . 

RUN pip install -r requirements.txt

ENTRYPOINT python app.py