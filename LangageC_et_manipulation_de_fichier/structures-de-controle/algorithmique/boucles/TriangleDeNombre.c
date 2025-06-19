#include <stdio.h>

void affichage(int nombre_de_lettre, int nombre_de_lettre_max, int nombre_de_ligne, int afficher) ;

void verification(int nombre_de_lettre, int nombre_de_lettre_max, int nombre_de_ligne, int afficher) {
	if (nombre_de_lettre != nombre_de_lettre_max) {
		nombre_de_lettre = 0;
		afficher = afficher + 1;
		affichage(nombre_de_lettre, nombre_de_lettre_max, nombre_de_ligne, afficher);
	}
	else {
		printf("\n \n 'FIN' \n");
	}
}

void affichage(int nombre_de_lettre, int nombre_de_lettre_max, int nombre_de_ligne, int afficher) {
	if (nombre_de_lettre != nombre_de_ligne) {
		printf("%d", afficher);
		nombre_de_lettre = nombre_de_lettre + 1;
		affichage(nombre_de_lettre, nombre_de_lettre_max, nombre_de_ligne, afficher);
	}
	else {
	printf("\n");
	nombre_de_ligne = nombre_de_ligne + 1; 
	verification(nombre_de_lettre, nombre_de_lettre_max, nombre_de_ligne, afficher);
	}
}

int main() {
	int afficher = 0;
	int nombre_de_lettre = 0;
	int nombre_de_ligne = 1;
	int nombre_de_lettre_max;
	printf("choisis un nombre de ligne :\n");
	scanf("%d", &nombre_de_lettre_max);
	printf("\n \n");
	verification(nombre_de_lettre, nombre_de_lettre_max, nombre_de_ligne, afficher);
}
