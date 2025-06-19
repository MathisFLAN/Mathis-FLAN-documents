#include <stdio.h>
#include <math.h>

void puissance2(double cote1, double cote2, double cote3) {
	cote1 = cote1 * cote1;
	cote2 = cote2 * cote2;
	cote3 = cote1 + cote2;
	cote3 = sqrt(cote3);
	printf("l'hypoténuse est égale à %lf \n", cote3);
	}

int main(){
    double cote1;
    double cote2;
    double cote3;
    printf("Saisir la valeur du premier cote \n");
    scanf("%lf", &cote1);
    printf("Saisir la valeur du deuxieme cote \n");
    scanf("%lf", &cote2);
    puissance2(cote1, cote2, cote3);
}
