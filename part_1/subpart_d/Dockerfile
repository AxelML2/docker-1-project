FROM python:3.9-slim

WORKDIR /usr/src/app

# copy whole app while being inside the folder (Dockerfile in this folder)
COPY app.py .
COPY process-data.py .  
COPY requirements.txt . 
COPY script.sh .
RUN pip install -r requirements.txt

CMD [ "/bin/bash","script.sh" ]