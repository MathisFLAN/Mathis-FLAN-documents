# base du shell

# exercice 1 :

```
Créer un script qui demande un nom de dossier (nom_dossier) et créer une arborescence dans ce nouveau dossier avec trois sous-dossiers bureau, documents, images.

La commande suivante permet de demander à l’utilisateur de saisir une réponse et stocke celle-ci dans la variable REPONSE

read -p "Saisir une réponse: " REPONSE
Plus d’information avec la commande help read

Exemple:

mon_beau_projet
├── documents
├── bureau
└── images
```

# ma version de l'exercice

```
sachant que nous sommes dans un nouveau dossier (~/base_du_shell).
On créer un fichier "exercice1.sh" dans lequel on entre le programme suivant :

"""
#!/bin/bash

read -p "Entrez le nom du dossier principal : " nom_dossier
mkdir "$nom_dossier"
cd "$nom_dossier"
mkdir bureau
mkdir document
mkdir image
echo "Vous avez créer les dossier suivant : $nom_dossier"
tree

fi
"""

ensuite, on peut passez à l'exécution du fichier (attention cependant à ce que les droits d'exécutions soient bien accorder).

chmod +x exercice1.sh (pour les droits d'exécutions)
./exercice1.sh

on rentre ensuite le nom du dossier (peu importe) et l'arborescence apparaitra
```

# commande read -p "Entrez le nom du dossier principal : " nom_dossier

```
permet de posez la question "Entrez le nom du dossier principal : " puis, ce que nous allons taper sera enregistré dans la variable $nom_dossier
```

# exercice 2 :

```
Créer un script qui demande un chemin vers un dossier et qui crée dans ce dossier un dossier travail.
```

```
dans le même dossier que l'exercice

"""
#!/bin/bash

read -p "Entrez le chemin recherché : " chemin

mkdir -p "$chemin/travail"
mkdir -p "$chemin/travail/windows"
mkdir -p "$chemin/travail/macos"
mkdir -p "$chemin/travail/linux"
tree

fi
"""

Si on est pas sur de l'écriture exact ou de l'emplacement du chemin, taper la commande : pwd
```

# différente lignes possibles dans un fichier sh :

```
-imposer une conditions :

if CONDITION
then
    COMMANDE
fi

vérifier si une commande a bien été exécuter :

if grep mathis /etc/passwd
then
    echo OK

fi

-vérifier si un fichier existe bien :

fichier=/tmp

if [[ -e $fichier ]]    (remplacer "-e" par "-d" si il s'agit d'un dossier + si vous cherchez l'évenement contraire, ajoutez "!" avant le "-e")
then
    echo "le fichier existe"
fi

-exécuter une commande ou une autre en cas d'échec de vérification de la condition :

if CONDITION
then
    COMMANDE_SI_CONDITION_VRAIE
else
    COMMANDE_SI_CONDITION_FAUSSE
fi

-écrire un commentaire :

#texte

on peut taper également plusieurs commandes sur la même ligne à condition qu'on les sépares avec un point virgule.

exemple :

echo bonjour ; echo salut
bonjour
salut
```

# exercice 3 :

```
Modifier le script de l’exercice 1 pour vérifier si le dossier existe avant de le créer
```

```
#!/bin/bash

read -p "Entrez le nom du dossier principal : " nom_dossier

if [[ -d $mon_dossier ]]
then
	echo "ce dossier existe déjà"
else
	mkdir "$nom_dossier"
	cd "$nom_dossier"
	mkdir bureau
	mkdir document
	mkdir image
	echo "Vous avez créer les dossier suivant : $nom_dossier"
	tree

fi
```

# exercice 4 :

```
Modifier le script de l’exercice 2 pour vérifier :

si le dossier de destination est inscriptible
si le dossier existe avant de le créer
```

```
#!/bin/bash

read -p "Entrez le chemin recherché : " chemin

if [[ -d $chemin ]]
then
	if [[ -w $chemin ]]
	then

		mkdir -p "$chemin/travail"
		mkdir -p "$chemin/travail/windows"
		mkdir -p "$chemin/travail/macos"
		mkdir -p "$chemin/travail/linux"
		tree
	fi
fi

ATTENTION : mettre un nombre de "fi" équivalent au nombre de "if"
```

# Variables

```
exercice :

Écrire un programme nommé convertir_html qui:

demande à l’utilisateur de saisir un nom de fichier en .md
vérifie que le fichier existe
s’il existe, exécute la commande pandoc permettant de générer un fichier html à partir de ce fichier avec le suffixe html.
```

```
programme :

read -p "Veuillez saisir le nom du fichier (.md) : " fichier

if [[ -f "$fichier" ]]; then
    pandoc -f markdown -t html "$fichier" -o "${fichier%.md}.html"
    echo "Conversion terminée : ${fichier%.md}.html"
else
    echo "Erreur : le fichier '$fichier' n'existe pas."
fi
```

# comment rediriger sa sortie dans un autre fichier

# afficher le programme d'un fichier

```
cat ./nom_fichier
```

```
en définissant une variable :

./nom_du_programme << nom_de_variable
>valeur
>nom_de_variable
```

```
exécuter un programme tout en gardant le résultat à afficher dans un fichier :
./nom_programme > nom_fichier << nom_variable
> contenu_variable
> nom_variable

exemple en reprenant l'exercice précédent :

./converti_html.sh > demo.txt << DEMO
> entrainement.md
> DEMO

Dans ce cas, on définit la variable DEMO pour qu'elle ait comme contenue le nom du fichier "entrainement.md".
Ensuite, on exécute le programme avec la variable DEMO choisie mais le résultat qui doit être afficher, soit "Conversion terminée : entrainement.html" ne sera pas afficher dans le terminal mais dans le fichier demo.txt.
```
