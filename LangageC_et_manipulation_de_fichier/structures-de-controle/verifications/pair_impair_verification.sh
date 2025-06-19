#!/bin/bash

valeur=$1
reference=$2

TMP_DIR=~/tmp
mkdir -p "$TMP_DIR"

gcc /home/mathis/FLAN-Mathis/structures-de-controle/algorithmique/fonctions/PairImpair.c -o "$TMP_DIR/PairImpair"

echo "$valeur" | "$TMP_DIR/PairImpair" > "$TMP_DIR/sortie_test"

if diff "$TMP_DIR/sortie_test" "$reference" > /dev/null
then 
    echo "le programme fonctionne"
    exit 0
else
    echo "le programme ne fonctionne pas"
    exit 1
fi

rm "$TMP_DIR/sortie_test"
