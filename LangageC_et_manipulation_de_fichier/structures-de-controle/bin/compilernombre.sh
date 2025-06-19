#!/bin/bash

for fichier_a_compiler in *.c
do
	echo ${fichier_a_compiler}
	gcc -o ${fichier_a_compiler%.c} ${fichier_a_compiler}
done
