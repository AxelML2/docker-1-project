- Bâtir l'image app 
```
docker build -t app .
```

- Lancer l'app
```
docker run -p 80:80 app
```

- Lancer l'app avec un bind-mount (pour écriture du fichier via l'url localhost:80/write_request )

```
docker run -p 80:80 -v $(pwd):/opt/demo/project app 
```


- Ajouter une variable environnementale

```
docker run -p 80:80 -e MSG_TO_WRITE="from container 1" -v $(pwd):/opt/demo/project app 
```

- Exercice II - 6

```python

import subprocess

subprocess.run('docker build -t img .', shell=True, text=True)
# pour tester un seuil
# subprocess.call("docker run -d -p 81:80 img", shell=True, text=True)

for i in range(10):
    port = 80 + i
    subprocess.call("docker run -d -p {port}:80 img", shell=True, text=True)
```