import os
import time

import pandas as pd


def clean_csv():
    ##############################
    # Sélection du fichier csv (raw)
    ##############################

    # On récupère tous les csv

    # 🚨 🚨 🚨
    # os.listdir()---> liste ce qu'il y dans le dossier courant
    # et os.listdir('var/opt/project') -> liste ce qu'il y a dans le dossier var/opt/project

    csv_filenames = [fn for fn in os.listdir("data/scraped/") if fn.endswith(".csv")]
    # on les classe par ordre croissant
    csv_filenames = sorted(csv_filenames)
    # on prend le dernier élément
    filename = csv_filenames[-1]

    ##############################
    # cleaning du fichier csv
    ##############################

    df = pd.read_csv(f"data/scraped/{filename}")

    # On supprime la colonne inutile
    df = df.drop("Unnamed: 0", axis=1)
    # On renomme les colonnes
    df.columns = ["rang", "title_fr", "title_vo", "réalisateur(s)", "année", "pays"]

    ##############################
    # Enregistrement
    ##############################

    # 🚨 🚨 🚨
    filename_new = f"cleaned_{filename}"
    os.makedirs("data/cleaned", exist_ok=True)
    # option index=False permettrait d'éviter de récréer Unnamed: 0
    df.to_csv(f"data/cleaned/{filename_new}")


while True:
    print(os.listdir())
    clean_csv()
    time.sleep(45)
