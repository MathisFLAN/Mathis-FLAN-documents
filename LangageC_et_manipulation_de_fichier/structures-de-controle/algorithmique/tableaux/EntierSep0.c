#include <stdio.h>

int main () {
	int tableau[201];
	int valeur = 0;
	for(int i = 0; i < 201; i ++ ) {
		tableau[i] = 0;
		valeur = valeur + 1;
		i = i + 1;
		tableau[i] = valeur;
	}
	printf("%d %d %d %d %d %d \n", tableau[0], tableau[1], tableau[87], tableau[88], tableau[199], tableau[200]);
}
