#include <stdio.h>

int main() {
	int valeur;
	printf("veuillez entrer une valeur : \n");
	scanf("%d", &valeur);
	valeur = valeur * valeur;
	printf("son carre est : %d \n", valeur);
}
