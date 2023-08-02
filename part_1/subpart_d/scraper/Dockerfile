FROM python:3.9-slim 

WORKDIR /usr/src/app

COPY scraper.py .

# copier tout le contenu du dossier courant
# dans le Working Directory :
# COPY . . 

RUN pip3 install lxml
RUN pip3 install pandas

CMD ["python", "scraper.py"]