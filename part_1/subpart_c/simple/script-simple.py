import datetime
import os
from urllib import request, parse
import ssl

import requests
import pandas as pd

def get_url_and_language():
    URL = os.environ.get("URL")
    LANGUAGE = os.environ.get("LANGUAGE")
    return URL, LANGUAGE


def get_table(URL):
    context = ssl._create_unverified_context()
    response = request.urlopen(URL, context=context)
    html = response.read()
    return pd.read_html(html)[0].iloc[1:-1, 0:2].dropna()


if __name__ == "__main__":
    URL, LANGUAGE = get_url_and_language()
    os.makedirs(LANGUAGE, exist_ok=True)
    table = get_table(URL)
    table.to_csv(f"{LANGUAGE}/wikipedia_table.csv")

    with open("logs.txt", "a") as f:
        now = datetime.datetime.now().isoformat()
        message = f"{now}: {LANGUAGE} data scraped\n"
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