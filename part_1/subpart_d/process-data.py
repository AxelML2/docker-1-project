import datetime
import time
import pandas as pd
import os

url = "https://fr.wikipedia.org/wiki/Top_250_de_l%27Internet_Movie_Database"

df = pd.read_html(url)[0]

while True:
    ### Etapes du scraper
    now = datetime.datetime.now().isoformat().replace(".", "_")
    filename = f"top_250_imdb_{now}.csv"
    os.makedirs("data/scraped", exist_ok=True)
    df.to_csv(f"data/scraped/{filename}")

    ### Etapes du cleaner
    csv_filenames = [fn for fn in os.listdir("data/scraped/") if fn.endswith(".csv")]
    csv_filenames = sorted(csv_filenames)
    file_name = csv_filenames[-1]
    df = pd.read_csv(f"data/scraped/{file_name}")
    df = df.drop("Unnamed: 0", axis=1)
    df.columns = ["rang", "title_fr", "title_vo", "réalisateur(s)", "année", "pays"]
    filename_new = f"cleaned_{file_name}"
    os.makedirs("data/cleaned", exist_ok=True)
    df.to_csv(f"data/cleaned/{filename_new}")
    time.sleep(45)