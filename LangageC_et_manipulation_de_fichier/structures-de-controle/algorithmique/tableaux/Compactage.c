#include <stdio.h>

int main () {
	int tableau[10] = {1, 0, 8, 5, 0, 5, 1, 0, 4, 5};
	int second_tableau[10];
	int valeur = 0;
	for(int h = 0; h < 10; h ++) {
		if (tableau[h] != 0) {
			second_tableau[valeur] = tableau[h];
			valeur = valeur + 1;
		}
	}
	printf("%d %d %d %d %d %d %d \n", second_tableau[0], second_tableau[1], second_tableau[2], second_tableau[3], second_tableau[4], second_tableau[5], second_tableau[6]);
}
