import datetime
import time
import pandas as pd
import os

url = "https://fr.wikipedia.org/wiki/Top_250_de_l%27Internet_Movie_Database"

df = pd.read_html(url)[0]

while True:
    # On prend la date en string : on remplace le point par un _
    now = datetime.datetime.now().isoformat().replace(".", "_")
    filename = f"top_250_imdb_{now}.csv"
    os.makedirs("data/scraped", exist_ok=True)
    df.to_csv(f"data/scraped/{filename}")
    time.sleep(60)
