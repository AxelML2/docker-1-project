### 1

- La commande pour bâtir l'image

```
docker build -t img_1b . 
```


- La commande pour lancer le conteneur sur la base de l'image

```
docker run img_1b 
```
### 2

```
VAR_1
```
- a cette valeur ( Some variable for 1 ) car il lui ai attribué un variable d'environnement

```
VAR_2
```
- a cette valeur ( vide ) car il n'a pas de variable d'environnement

- J'ai corrigé et supprimer pour avoir ce résultat :

```Dockerfile

FROM busybox

ENV VAR_1="Some variable for 1"

ENV VAR_2="Some variable for 2"

RUN export VAR_2="Some variable for 2"

CMD echo FOO is $VAR_1, BAR is $VAR_2
```

![Alt text](image.png)

### 3.

- J'ai donc enlevé les variables d'environnement dans le Dockerfile-corrected :

```Dockerfile

FROM busybox

RUN export VAR_2="Some variable for 2"

CMD 
```

- puis j ai run avec les variables d environnements

```
docker run -e VAR_1='Some variable for 1' -e VAR_2='Some variable for 2' img_1bcorrecter
```

![Alt text](image-1.png)


- Voici à quoi ressemble le "Dockerfile-corrected" :

```Dockerfile
FROM busybox

CMD echo FOO is $VAR_1, BAR is $VAR_2
``` 


