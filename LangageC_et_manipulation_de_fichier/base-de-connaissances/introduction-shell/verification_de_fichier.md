```
les fichier en question se trouvent dans le dossier : FLAN-Mathis/structures-de-controle/verifications/
```

# exemple de programme vérifiant un programme en langage C :

# Programme Pair Impair en langage C

```
#include <stdio.h>

int est_pair(int nombre) {
	return nombre % 2 == 0;
}

void pair_ou_impair(int nombre) {
	if(est_pair(nombre)) {
		printf("Ce nombre est pair\n");
	}
	else {
		printf("Ce nombre est impair\n");
	}
}

int main(){
    int nombre;
    printf("Saisir une chiffre \n");
    scanf("%d", &nombre);
    pair_ou_impair(nombre);
}
```

# programme de verifications

```
#!/bin/bash

valeur=$1
reference=$2

TMP_DIR=~/tmp
mkdir -p $TMP_DIR

gcc /home/mathis/FLAN-Mathis/structures-de-controle/PairImpair.c -o PairImpair
./PairImpair > $TMP_DIR/sortie_test <<chiffre
$valeur
chiffre

if diff $TMP_DIR/sortie_test $reference
then 
	echo "le programme fonctionne"
	exit 0
else
	echo "le programme ne fonctionne pas"
	exit 1
fi

rm $TMP_DIR/sortie_test
```

# programme pour faire plusieurs tests en même temps

```
#!/bin/bash

tester(){
        programme=$1
        valeur=$2
        reference=$3
        if $programme $valeur $reference > /dev/null
        then
                echo "test $programme $valeur $reference OK"
        else
                echo "test $programme $valeur $reference KO"
        fi
}

tester ./pair_impair_verification.sh 15 reference_impair.txt
tester ./pair_impair_verification.sh 57 reference_impair.txt
tester ./pair_impair_verification.sh 56 reference_pair.txt
tester ./pair_impair_verification.sh 29 reference_pair.txt
```

# Attention : un seul texte dois s'afficher à chaque fois : 

```
exemple : test ./pair_impair_verification.sh 15 reference_impair.txt OK ou encore test ./pair_impair_verification.sh 29 reference_pair.txt KO
```

# explications :

```
-Dans tout_tester.sh :

il faut d'abord savoir qu'une fois le pprogramme tester() créer, les lignes tester ./pair_impair... sont programmer de façon à définir les
variables programmes, valeur et references soit définis en même temps que ...

echo "test $programme $valeur $reference OK" ou "test $programme $valeur $reference KO"

> dev/null


-Dans pair_impair_verifications.sh :

variable valeur et references

TMP_DIR=~/tmp
mkdir -p $TMP_DIR

gcc /home/mathis/FLAN-Mathis/structures-de-controle/PairImpair.c -o PairImpair

./PairImpair > $TMP_DIR/sortie_test <<chiffre
$valeur
chiffre

if diff $TMP_DIR/sortie_test $reference
then 
	echo "le programme fonctionne"
	exit 0
else
	echo "le programme ne fonctionne pas"
	exit 1
fi


Voici un exemple d'exécution du programme tout_tester.sh et son résultat :
--------------------------------------------------------------------------
$ ./tout_tester.sh
test ./pair_impair_verification.sh 15 reference_impair.txt OK
test ./pair_impair_verification.sh 57 reference_impair.txt OK
test ./pair_impair_verification.sh 56 reference_pair.txt OK
test ./pair_impair_verification.sh 29 reference_pair.txt KO
--------------------------------------------------------------------------
```

# Bonus : ajouter le nombre de tests effectués, réussis et échoués, puis en faire un tableau sur les noms de tests et leurs état :

```
Pour cela, il a simplement suffit d'améliorer le programme tout_tester.sh de la sorte :
---------------------------------------------------------------------------------------
#!/bin/bash

declare -a noms_tests
declare -a etats_tests

declare nb_tests_effectues #ceci n'est pas obligatoire
declare nd_tests_reussis
declare nd_tests_echoues
nd_tests_effectues=0
nd_tests_reussis=0
nd_tests_echoues=0

tester(){
        programme=$1
        valeur=$2
        reference=$3
        noms_tests+=("$programme $valeur")
        if $programme $valeur $reference > /dev/null
        then
                echo "test $programme $valeur $reference OK"
		(( nb_tests_reussis = nb_tests_reussis + 1 ))
		etats_tests+=("OK")
        else
                echo "test $programme $valeur $reference KO"
                (( nb_tests_echoues = nb_tests_echoues + 1 ))
                etats_tests+=("KO")
        fi
}

		      #programme   valeur  reference
tester ./pair_impair_verification.sh 15 reference_impair.txt
tester ./pair_impair_verification.sh 57 reference_impair.txt
tester ./pair_impair_verification.sh 56 reference_pair.txt
tester ./pair_impair_verification.sh 29 reference_pair.txt
tester ./pair_impair_verification.sh 30548 reference_impair.txt
tester ./pair_impair_verification.sh 5459 reference_pair.txt

(( nb_tests_effectues = nb_tests_echoues + nb_tests_reussis ))

echo "nb_tests_effectues = $nb_tests_effectues"
echo "nb_tests_reussis = $nb_tests_reussis"
echo "nb_tests_echoues = $nb_tests_echoues"

for (( i=0; i<${#noms_tests[@]}; i++))
do
        echo "|   ${noms_tests[$i]}   |  ${etats_tests[$i]}  |"
done
```
