#!/bin/bash

#for fichier in *.md
#do
#	echo ${fichier}
#	pandoc -f markdown -t html ${fichier} -o ${fichier%.md}.html
#done

read -p "Veuillez saisir le nom du fichier (.md) : " fichier

if [[ -f "$fichier" ]]; then
	pandoc -f markdown -t html "$fichier" -o "${fichier%.md}.html"
	echo "Conversion terminée : ${fichier%.md}.html"
else
	echo "Erreur : le fichier '$fichier' n'existe pas."
fi
