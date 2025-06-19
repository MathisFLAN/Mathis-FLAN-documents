# Commande ls

```
Permet d'afficher les noms de dossier et fichier se trouvant dans le document choisi.
```

# Commande ls -l

```
C'est comme ls mais en plus cela affiche le type de fichier / dossier, les droits du fichier pour les users/groupe/others, le propriétaire, sa dernière date de modification et son nom entier.
```

# Commande ls -R

```
Affiche absolument tous le contenu des dossier et sous dossier.
```

# Commande apt-get install tree

```
Permet d'installer la commande tree dans le terminal (celle ci va nous permettre d'afficher des arboréscence de nos dossier.
```

# Commande mkdir racine

```
créer un dossier du nom de "racine".
```

# Commande cd racine

```
Permet d'entrer dans le dossier racine.
```

# Commande mkdir branche.est branche.sud-est branche.nord-est

```
Permet de créer les dossier branche.est, branche.sud-est et branche.nord-est en même temps dans le dossier où nous sommes.
```

# Commande cd

```
Fais revenir au point de départ (en d'autres termes, dans les dossier home)
```

# Commande pwd

```
affiche le dossier dans lequel nous sommes et dans quels autres dossier celui ci se trouve.
```
# Application

```
-déplacez-vous dans la branche Sud-Est.
cd branche.sud-est
-allez directement dans la branche Nord-Est
cd
cd racine/branche.nord-est/
-allez sur le tronc gauche et créez les branches Ouest, Sud-Ouest et Nord-Ouest
cd tronc.gauche
mkdir branche.ouest branche.sud-ouest branche.nord-ouest
```

# Commande touch nom_fichier

```
Permet de créer un fichier vide du nom et du format donner par l'utilisateur.
```

# Exercices

```
-Affichez les fichiers de votre répertoire utilisateur.
cd
ls
-Créez un fichier appelé ancien, sans utiliser un éditeur de texte.
Nous cliquons sur les document, assurons de bien être dans les dossiers personnel puis, il faut faire clic droit, "Créer un nouveau fichier" que nous allons nommé ancien.
-Copiez le fichier ancien vers un fichier appelé nouveau.
cp ancien nouveau
-Effacez le fichier ancien.
cd nouveau
rm ancien
-Vérifiez l’effacement.
nous allons dans le dossier nouveau, et si il n'y est plus, l'effacement est affirmé.
-Créez un répertoire appelé : repertoireAvecUnNomSuperLongPourNePasAvoirEnvieDeLeTaperPlusDUneFois.
mkdir repertoireAvecUnNomSuperLongPourNePasAvoirEnvieDeLeTaperPlusDUneFois
En sachant que il vaut mieux copier coller le nom pour être sur qu'il soit correct.
-Vérifiez sa présence.
En parcourant les dossier, si un autre porte le nom donner précédement, alors le répertoire est créer.
-Déplacez vous dans ce répertoire [*].
cd repertoireAvecUnNomSuperLongPourNePasAvoirEnvieDeLeTaperPlusDUneFois
-Copiez le fichier nouveau dans ce répertoire.
cp fichier repertoireAvecUnNomSuperLongPourNePasAvoirEnvieDeLeTaperPlusDUneFois/
-Revenez dans votre home directory (3 solutions)
cd
cd $home
cd ~
-Effacez le répertoire que vous avez créé précédemment.
rm -r repertoireAvecUnNomSuperLongPourNePasAvoirEnvieDeLeTaperPlusDUneFois/
-Vérifiez la suppression.
ls
si le dossier n'y est plus, alors la suppression a été operationnelle
```
