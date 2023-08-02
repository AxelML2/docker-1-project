### Création du volume

```bash
docker volume create storage
```


### Build et run du scraper
```bash
docker build -t scraper . 
```

```bash
docker run -v storage:/usr/src/app/data scraper
```

### Build et run du cleaner
```bash
docker build -t cleaner . 
```

```bash
docker run -v storage:/usr/src/app/data cleaner
```


### Build et run de l'app
```bash
docker build -t app . 
```

```bash
docker run -p 80:80 -v storage:/usr/src/app/data app
```



- Lancer l'app avec un bind-mount (pour écriture du fichier via l'url localhost:80/write_request )

```
docker run -p 80:80 -v 
```



### Vérification

**ON DOIT UTILISER UN AUTRE CONTENEUR POUR VERIFIER SI LES DONNEES SONT DANS LE VOLUME**

```bash
docker run -it -v storage:/usr/src/app/data bash
cd usr/src/app/data
ls scraped
ls cleaned
```





