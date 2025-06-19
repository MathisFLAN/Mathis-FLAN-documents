#include <stdio.h>
#include <math.h>

int main() {
	int puissance = 7;
	int chiffre;
	int resultat[9];
	int difference;
	printf("Choisissez un chiffre : \n");
	scanf("%d", &chiffre);
	while (puissance > 0) {
		difference = 1;
        	int h;
        	for (h = 0; h < puissance; h++) {
        		difference = difference * 2;
        		}
                if (chiffre >= difference) {
        		chiffre -= difference;
        		resultat[puissance] = 1;
        		}
        	else {
        		resultat[puissance] = 0;
        		}
		puissance -= 1;
		}
	printf("Résultat en base 2 : ");
	for (int i = 8; i >= 0; i--) {
		printf("%d", resultat[i]);
    		}	
	printf("\n");
}
