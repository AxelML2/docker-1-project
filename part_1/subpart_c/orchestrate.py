import subprocess;
import time;

process=subprocess.Popen(["powershell",'docker build -f .\simple\Dockerfile -t img_1csimple .'])
time.sleep(2)
process=subprocess.Popen(["powershell",f'docker run --rm -e URL="https://fr.wikipedia.org/wiki/Python_(langage)" -e LANGUAGE="python" -v $pwd/python:/usr/src/app/python img_1csimple'])
time.sleep(2)
process=subprocess.Popen(["powershell",f'docker run --rm -e URL="https://fr.wikipedia.org/wiki/JavaScript" -e LANGUAGE="javascript" -v $pwd/javascript:/usr/src/app/javascript img_1csimple'])