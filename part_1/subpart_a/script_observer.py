import os 
import datetime
import time

OBSERVED = os.environ.get("OBSERVED")

while True:
    now = datetime.datetime.now()
    current_content = os.listdir(OBSERVED)
    print(f"Contenu du dossier observed : {current_content} à cette date : {now}")
    time.sleep(5)