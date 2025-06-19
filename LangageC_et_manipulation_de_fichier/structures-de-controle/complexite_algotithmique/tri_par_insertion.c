#include <stdio.h>

void classement(int tableau[], int taille) {
	for (int h = 1; h < taille; h++) {
		int cle = tableau[h];
		int j = h - 1;

		while (j >= 0 && tableau[j] > cle) {
			tableau[j + 1] = tableau[j];
			j = j - 1;
		}
		tableau[j + 1] = cle;
	}
}

int main() {
	int tableau[15] = {9, 5, 36, 8, 88, 6, 1, 97, 2, 10, 4, 7, 15, 99, 3};
	int taille = sizeof(tableau) / sizeof(tableau[0]);
	classement(tableau, taille);
	printf("Tableau après le tri :\n");
	for (int i = 0; i < taille; i++) {
		printf("%d ", tableau[i]);
	}
	printf("\n");
}
