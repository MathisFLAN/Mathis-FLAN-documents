#include <stdio.h>

void affichage(int nombre_de_lettre, int nombre_de_lettre_max, int nombre_de_ligne) ;

void verification(int nombre_de_lettre, int nombre_de_lettre_max, int nombre_de_ligne) {
	if (nombre_de_lettre != nombre_de_lettre_max) {
		nombre_de_lettre = 0;
		affichage(nombre_de_lettre, nombre_de_lettre_max, nombre_de_ligne);
	}
	else {
		printf("\n \n 'FIN' \n");
	}
}

void affichage(int nombre_de_lettre, int nombre_de_lettre_max, int nombre_de_ligne) {
	if (nombre_de_lettre != nombre_de_ligne) {
		printf("h");
		nombre_de_lettre = nombre_de_lettre + 1;
		affichage(nombre_de_lettre, nombre_de_lettre_max, nombre_de_ligne);
	}
	else {
	printf("\n");
	nombre_de_ligne = nombre_de_ligne + 1; 
	verification(nombre_de_lettre, nombre_de_lettre_max, nombre_de_ligne);
	}
}

int main() {
	int nombre_de_lettre = 0;
	int nombre_de_ligne = 1;
	int nombre_de_lettre_max;
	printf("choisis un nombre de ligne :\n");
	scanf("%d", &nombre_de_lettre_max);
	printf("\n \n");
	verification(nombre_de_lettre, nombre_de_lettre_max, nombre_de_ligne);
}
