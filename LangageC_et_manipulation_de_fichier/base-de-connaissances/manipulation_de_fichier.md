# Manipulation de fichier
# Récupération des fichiers de travail

```
-Créer un répertoire tpfichiers et se placer dans ce répertoire pour réaliser les exercices proposés ci-dessous.

mkdir tpfichiers
cd tpfichiers

-Vous allez télécharger le fichier manipulation-fichiers.tar.gz en utilisant la commande wget.
Pour cela cliquer bouton droit sur le lien ci-dessus et copier l’adresse du lien
Ensuite, coller cette adresse dans la commande suivante:

wget https://tstn1.aezi.fr/b1-24-25/data/manipulation-fichiers.tar.gz

-Décompressez ce fichier avec une commande tar appropriée. Placez-vous ensuite dans le répertoire extrait: vous êtes prêt pour la suite.

tar -xvzf manipulation-fichiers.tar.gz
```

# Exemples de commandes ls :
# commande ls -A

```
permet d'afficher tous les dossiers, y compris les dossiers cachés, c'est à dire ceux commençant par "." ou "..".
```

# commande ls -d

```
permet d'afficher uniquement les répertoires mais en plus leur contenu.
```

# commande ls -F + ... :
#/

```
permet d'afficher tous les dossiers.
```

#*

```
permet d'afficher tous les fichiers éxecutables.
```

#@

```
permet d'afficher tous les liens symboliques.
```

# commande ls -R

```
Affiche tous les sous-dossiers et fichiers du répertoires
```

# commande ls -a

```
C'est comme la commande ls -A à la différence qu'elle n'affiche que les fichiers commençant par "." uniquement. (Elle vraiment beaucoup moins efficace.
```

# commande ls -l

```
permet d'afficher les fichiers sous forme de liste détaillée avec permissions, propriétaire, groupe, taille et date de modification.
```

# commande wc

```
permet de compter les éléments dans un fichier ou dans l’entrée standard (stdin).
```

# par exemple

```
dans un fichier nombres.txt :
Un deux trois
Quatre
Cinq six

puis si on tape cat nombres.txt | wc
Ceci indique que le fichier contient :
3 lignes
6 mots
30 caractères
```

# commande wc

```
permet de compter les éléments dans un fichier ou dans l’entrée standard (stdin).
```

# Options supplémentaire pour la commande wc : 
# commande wc -c

```
Affiche le nombre de caractères contenu dans le fichier.
```

# commande wc -l

```
Affiche le nombre de lignes contenu dans le fichier.
```

# commande wc -w

```
Affiche le nombre de mots contenu dans le fichier.
```

# Options supplémentaires pour la commandes echo
# commande echo lettre*

```
Affiche tous les dossier dont le nom commençant par la lettre choisie.
```

# commande echo *lettre*

```
Affiche tous les dossier dont le nom commence/contient/se_termine par la lettre choisie.
```

# commande echo ??lettre*

```
Affiche tous les dossier dont le nom commence par exactement 2 caractères suivi d'un r à la suite.
```

# commande echo [rm]o*

```
Affiche tous les dossiers commençant par la lettre r ou m suivie d'un o.
```

# exécution, affichage
```
-Exécutez le fichier init (qui crée un répertoire unix et des fichiers et dossiers à l’intérieur de ce répertoire)

cd tpfichiers/premiersPas/
ls -l init
(si le droit d'exécution n'est pas accorder) : chmod u+w init
./init

-Combien de fichiers ont été créés ?

ls -A | wc -l
51 fichiers ont été créer

-En êtes vous sûr ?

pourtant j'endoute car je n'en voit que 41, à moins qu'il ai ajouté des fichiers qu'on ne peut pas voir. En effet, lorsqu'on tape "ls -A", on s'apperçoit qu'il y a plus de fichier afficher.

-Combien de répertoires ont été créés ?

6 repertoires ont été créer.

-Listez tous les fichiers dont le nom contient un F.

echo *f*

-Listez tous les fichiers dont le nom contient deux chiffres.

echo *[0-9]*[0-9]*

-Listez tous les fichiers dont le nom contient deux chiffres côte à côte.

echo *[0-9][0-9]*

-Effacez tous les fichiers dont le nom fini par d.

rm *d

-Copiez tous les fichiers dont le nom contient un 1 ou un 3 dans un sous-répertoire nommé copy (créez le si nécessaire).

mkdir -p copy
cp -r *[13]* copy

-Mettez, dans un fichier nommé listeComplete.txt, la liste de tous les fichiers créés par le script init.

touch listeComplete.txt
ls -A | grep -v copy > listeComplete.txt
ls -Ad .tmp* tmp* > listeComplete.txt
echo .tmp* tmp* > listeComplete.txt

-Déplacez-le dans le répertoire de base de votre compte.

(dans le même dossier que celui ci) mv listeComplete.txt ~

-Utiliser la commande tree -a pour vérifier si vous aviez bien vu tous les fichiers créés.

-Utiliser la commande file sur chaque fichier pour vérifier à quel type il correspond.

file tmp.1BnzW9ByGE (tmp.1BnzW9ByGE: Unicode text, UTF-8 text)
file tmp.1IVllqHLTW (tmp.1IVllqHLTW: Unicode text, UTF-8 text)
file tmp.1uvxw7BXTM (tmp.1uvxw7BXTM: Unicode text, UTF-8 text)
file tmp.21ibgffT9B (tmp.21ibgffT9B: Unicode text, UTF-8 text)
file tmp.3ViU5FWb5t (tmp.3ViU5FWb5t: Unicode text, UTF-8 text)
file tmp.48wYRfkz3c (tmp.48wYRfkz3c: Unicode text, UTF-8 text)
file tmp.OC46KvGe8r (tmp.OC46KvGe8r: PDF document, version 1.5)
file tmp.4f9QI4tDaA (tmp.4f9QI4tDaA: Unicode text, UTF-8 text)
file tmp.4Hu6K7zqbV (tmp.4Hu6K7zqbV: Unicode text, UTF-8 text)
file tmp.4sLqTDRs7Z (file tmp.4sLqTDRs7Z)
file tmp.5IxL1Rt4iU (tmp.5IxL1Rt4iU: Unicode text, UTF-8 text)
file tmp.5lqgYMhtRT (tmp.5lqgYMhtRT: Unicode text, UTF-8 text)
file tmp.5yfY3KiVZA (tmp.5yfY3KiVZA: Unicode text, UTF-8 text)
file tmp.63mE6w1aoZ (tmp.63mE6w1aoZ: Unicode text, UTF-8 text)
file tmp.apGmUZLFix (tmp.apGmUZLFix: empty)
file tmp.bj9f5XuPKG (tmp.bj9f5XuPKG: Unicode text, UTF-8 text)
file tmp.bow4OiAvD7 (tmp.bow4OiAvD7: Unicode text, UTF-8 text)
file tmp.eAAqcUuOSi (tmp.eAAqcUuOSi: empty)
file tmp.1quHGMChUf (tmp.1quHGMChUf: PDF document, version 1.5)
file tmp.eDJGgMCmNr (tmp.eDJGgMCmNr: Unicode text, UTF-8 text)
file tmp.eEwRJ784Gu (tmp.eEwRJ784Gu: Unicode text, UTF-8 text)
file tmp.ENOhOTSnHp (tmp.ENOhOTSnHp: Unicode text, UTF-8 text)
file tmp.guXQ8MaAK6 (tmp.guXQ8MaAK6: Unicode text, UTF-8 text)
file tmp.iibuS7u6XH (tmp.iibuS7u6XH: empty)
file tmp.jbk4Np3e1B (tmp.jbk4Np3e1B: Unicode text, UTF-8 text)
file tmp.K8lDVk5dhZ (tmp.K8lDVk5dhZ: Unicode text, UTF-8 text)
file tmp.NZygz4pONg (tmp.NZygz4pONg: Unicode text, UTF-8 text)
file tmp.oZdSKlAAyO (tmp.oZdSKlAAyO: empty)
file tmp.PMes5mNpiN (tmp.PMes5mNpiN: Unicode text, UTF-8 text)
file tmp.pWsj9KaZrQ (tmp.pWsj9KaZrQ: empty)
file tmp.qemAvFV9Bp (tmp.qemAvFV9Bp: Unicode text, UTF-8 text)
file tmp.S7r8tzgtIw (tmp.S7r8tzgtIw: empty)
file tmp.u7EC608pei (tmp.u7EC608pei: Unicode text, UTF-8 text)
file tmp.ug14WASaRW (tmp.ug14WASaRW: Unicode text, UTF-8 text)
file tmp.ukLqrXSHTe (tmp.ukLqrXSHTe: Unicode text, UTF-8 text)
file tmp.VntWrMxSir (tmp.VntWrMxSir: Unicode text, UTF-8 text)
file tmp.vtmoxwvfX9 (tmp.vtmoxwvfX9: Unicode text, UTF-8 text)
file tmp.WsfhPWlmGW (tmp.WsfhPWlmGW: empty)
file tmp.X8s4qX5crS (tmp.X8s4qX5crS: empty)
file tmp.xDChKhCSPW (tmp.xDChKhCSPW: Unicode text, UTF-8 text)
file tmp.xGNzVGvn0P (tmp.xGNzVGvn0P: empty)
file tmp.YMDaUgbiwV (tmp.YMDaUgbiwV: Unicode text, UTF-8 text)
file tmp.ZkInLhr9tE (tmp.ZkInLhr9tE: Unicode text, UTF-8 text)
```

# Manipulation de répertoir et de fichiers

```
-Effacez le répertoire unix créé par le script init. Fermez le terminal, et ouvrez de nouveau un terminal. Cette partie se fait uniquement -par la ligne de commande.



-Vérifier où on se trouve dans l’arborescence des fichiers (répertoire courant)



-Se déplacer à la racine du disque. Lister les répertoires existants.



-Se déplacer dans votre répertoire de travail par défaut (3 solutions possibles, notez-les !!!).



-Créer un répertoire de nom UNIX.



-Sous UNIX créer un répertoire de nom TP1.



-Aller dans le dernier répertoire créé.



-Créer un répertoire de nom tmp.



-Aller dans le répertoire tmp.



-Créer un fichier vide nommé vide.txt.



-Lister l’arborescence du répertoire UNIX en format long.



-Remonter d’un niveau dans l’arborescence.



-Détruire le répertoire tmp avec la commande rmdir.



-Que se passe-t-il ?



-Faites en sorte de détruire ce répertoire.



-Retourner dans le répertoire tpfichiers.



-Prendre le fichier dessus.txt et le copier dans le répertoire de base de votre compte utilisateur.



-Visualiser le fichier dessus.txt à l’aide de la commande cat.



-Le visualiser à l’aide de la commande more. Quelles sont les différences ?



-Faire de même avec la commande less (pour quitter less, appuyer sur la touche Q).



-Le rouvrir avec la commande less. Rechercher le mot locataire.



-Recréer le répertoire tmp.



-Faire une copie du fichier dessus.txt dans le répertoire tmp.



-Aller dans le répertoire tmp et renommer le fichier dessus.txt en Dessous.txt.



-Le déplacer dans le répertoire de base de votre compte.



-Vérifier que le fichier s’y trouve bien.


```
