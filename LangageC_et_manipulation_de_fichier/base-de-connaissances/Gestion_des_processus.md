# commande sleep "chiffre"

```
Permet de bloquer le terminal pendant un certain temps (chiffre).
Si c'est trop long, on peut utiliser ctrl + c pour annuler la commande
```

# commande sleep 5

```
Permet de bloquer le terminal pendant 5 secondes.
```

# commande sleep 3600

```
Permet de bloquer le terminal pendant une heure, mais celle ci est exécuter dans le background.
```

# commande ps

```
affiche en détails les informations sur les processus.
```

# commande ps -elf | grep sleep

```

affiche en détails les informations sur les processus qui contiennent la commande sleep.
```

# Mais si on la remplace par la commande ps -elf | head -1 ; ps -elf | grep sleep

```
Cela affichera en détails les informations sur les processus qui contiennent la commande sleep. Mais en plus, nous aurons précisément la signification de chaques collones
```

# commande ps aux | grep sleep

```
Même principe que la commande ps -elf | grep sleep, mais l'affichage sera en revanche différent.
```

# commande kill PID ou Job_number

```
Permet D'arrêter la dernière commande éxecuter, en fonction soit du pid et du numéro du job entrer
```

# ctrl z (après avoir exécuter une commande type sleep 3600) 

```
Envoie la commande en cours d'exécution dans le background.
```

# bg 

```
Permet d'exécuter une commande dans le background.
```

# fg 

```
ramène la dernière commande au premier plan
```

# wget lien_du_site 

```
Permet de témécharger un fichier depuis un certain site internet.
```

# si on combine cela avec bg puis un peu plus tard, tail wget-log 

```
On peut voir si la progression du téléchargement du fichier est bien avancée ou non.
```

# Installer le paquet x11-apps et lancer par exemple les commandes suivantes:
  xeyes, xclock, xman.
```
sudo apt install x11-apps
```
```
xeyes = fais apparaitre une fenêtre ou les yeux suivent le curseur
xclock = fais apparaitre une fenêtre avec une horloge programmer à l'heure actuelle
xman = fais apparaitre une fenêtre présentant une interface graphique pour afficher les pages de manuel
```
# commande top

```
affiche en temps réel les processus en cours d'exécution sur Linux
```

# commande screen
#

```
ouvre un nouveau terminal permettant de lancr des processus dans une session détachable et ré-attachable.

Pour en sortir, il faut appuyer successivement sur ctrl a puis b
```

# commande screen -ls

```
Affiche la liste des screen en cours d’exécution

en fonctione de leurs chiffre, on peut faire la commande suivante :
```

# Pour se détacher d'un screen, on peut faire "ctrl a" puis ":", et taper "detach"
# commande screen -r nom_du_screen

```
permet de s'attacher de nouveau à une session screen portant se numéro.
```

# commande screen -d -r nom_du_screen

```
permet de s'attacher de nouveau à une session screen portant se numéro tout en se déconnectant d'une autre session.
```

# ls -R /

```
Cela permet d'afficher tous les fichiers du système de façon récursive (attention car sa va très vite).
```
