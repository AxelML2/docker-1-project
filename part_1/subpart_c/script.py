import datetime
import os
from urllib import request, parse
import ssl

import requests
import pandas as pd

# Ajout de la page wikipedia de du langage php 
urls = {
    "python": "https://fr.wikipedia.org/wiki/Python_(langage)",
    "javascript": "https://fr.wikipedia.org/wiki/JavaScript",
    "php": "https://fr.wikipedia.org/wiki/PHP",
}


def get_table(url):
    context = ssl._create_unverified_context()
    response = request.urlopen(url, context=context)
    html = response.read()
    return pd.read_html(html)[0].iloc[1:-1, 0:2].dropna()


if __name__ == "__main__":
    for language, url in urls.items():
        os.makedirs(language, exist_ok=True)
        table = get_table(url)
        table.to_csv(f"{language}/wikipedia_table.csv")

        with open("logs.txt", "a") as f:
            now = datetime.datetime.now().isoformat()
            message = f"{now}: {language} data scraped\n"
            print(message)
            f.write(message)

    ############################# question 4
    
    URL_LOGS = "http://host.docker.internal:80/get_request" ### URL qui permettra d'accéder a notre app qui répond seulement à des requêtes "POST".

    with open("logs.txt", "r") as f:
        try:
            response = requests.post(URL_LOGS, json={"logs": f.read()})

            print("Status code", response.status_code)
            print(response.json())

        except Exception as e:
            print(e)
