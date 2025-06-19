#include <stdio.h>

void affichage(int nombredelettre) {
	if (nombredelettre != 0) {
		printf("h");
		nombredelettre = nombredelettre - 1;
		affichage(nombredelettre);
	}
	else {
	printf("\n");
	}
}

int main() {
	int nombredelettre;
	printf("choisis un chiffre :\n");
	scanf("%d", &nombredelettre);
	affichage(nombredelettre);
}
