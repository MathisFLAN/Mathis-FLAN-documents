# Les dossiers utilisés sont les suivants :

```
entrainement/PATH/

nombre.c


$HOME/bin

compilernombre.sh
```

# Comment créer le fichier dexécution d'un fichier.c ?

```
-On créer les fichiers (nombre.c dans PATH et compilernombre dans bin) et on leur ajoute un programme
-depuis le dossier PATH, taper : nano $HOME/bin/compilernombre.sh
-puis on le complète comme so dessous :
#!/bin/bash

gcc -o nombre nombre.c

-ensuite assurons nous que les fichiers soient bien exécutables. Sinon ajouter les permissions avec chmod +x
-taper : PATH=$PATH:$HOME/bin
-Ensuite taper le nom du fichier "compilernombre.sh" depuis le dossier PATH.
```

# comment le faire pour plusieurs fichiers.c en même temps ?

```
il suffit de faire la même chose mais dans le fichier "compilernombre.sh" il faut ajouter le programme suivant :

#!/bin/bash

for fichier_a_compiler in *.c
do
	echo ${fichier_a_compiler}
	gcc -o ${fichier_a_compiler%.c} ${fichier_a_compiler}
done

Ensuite, pensez à ce que ce fichier soit exécutable
```

# comment convertir un fichier md en html avec pandoc ?

```
Tout d'abord il faut avoir créer un fichier.md, une fois cela terminer
ATTENTION : si la date de modification d'un fichier est plus récente que celle du fichier
```
