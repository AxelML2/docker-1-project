- Bâtir l'image app 
```
docker build -t app .
```
- création d'un volume
```
docker volume create dst
```

- Lancer l'app
```
docker run -e SRC='./src' -e DST='./dst' -v dst:/usr/src/app img_1a
```

- Vérification avec un ls dans le volume "dst" dans le repertoire dst
```
docker run -v dst:/usr/src/app bash -c "ls /usr/src/app/dst"
```

![Alt text](image.png)

- le script n’attende plus après avoir fait la copie.
```
j'ai enlevé le time.sleep(10000)
```