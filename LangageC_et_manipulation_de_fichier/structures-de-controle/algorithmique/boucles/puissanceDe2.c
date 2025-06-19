#include <stdio.h>

int main() {
	int retour = 2;
	int valeur = 1;
	int chiffre = 1;
	while (chiffre < 11) {
		while (retour <= chiffre) {
			valeur = valeur * 2;
			retour = retour + 1;
		}
		printf("%d \n", valeur);
		retour = 2;
		valeur = 1;
		chiffre = chiffre + 1;
	}
}
