#include <stdio.h>

int main() {
	double pression = 14.5038;
	double chiffre;
	double resultat;
	double fois = 0;
	printf("choisissez un chiffre : \n");
	scanf("%lf", &chiffre);
	printf("Bar \t Psy \n");
	while (fois <= chiffre) {
		resultat = fois * pression;
		printf("%lf \t %lf \n", fois, resultat);
		fois = fois + 0.2;
	}
}

