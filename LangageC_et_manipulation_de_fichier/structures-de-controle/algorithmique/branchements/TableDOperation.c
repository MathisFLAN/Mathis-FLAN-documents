#include <stdio.h>

void operation(int chiffre, char operant, int fois, int resultat) {
	switch(operant) {
		case '+' :
			resultat = chiffre + fois;
			printf("%d + %d = %d \n", chiffre, fois, resultat);
			break;
		case '-' :
			resultat = chiffre - fois;
			printf("%d - %d = %d \n", chiffre, fois, resultat);
			break;
		case '*' :
			resultat = chiffre * fois;
			printf("%d * %d = %d \n", chiffre, fois, resultat);
			break;
	}
}

int main() {
	int fois = 0;
	int resultat = 0;
	int chiffre;
	printf("choisissez un chiffre : \n");
	scanf("%d", &chiffre);
	char operant;
	printf("choisissez un operant : \n");
	scanf(" %c", &operant);
	while (fois != 11) {
		operation(chiffre, operant, fois, resultat);
		fois = fois + 1; 
	}
}
