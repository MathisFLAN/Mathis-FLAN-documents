#include <stdio.h>

int main() {
	int chiffre;
	printf("choisissez un nombre : \n");
	scanf("%d", &chiffre);
	printf("\n \n"); //cette commande sert à mieux lire le résultat.
	while (chiffre != 0) {
		printf("%d \n", chiffre);
		chiffre = chiffre - 1;
	}
	printf("0 \n");
}
