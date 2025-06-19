#include <stdio.h>

int positifnegatif(int nombre) {
	return nombre >= 0;
}

void verification(int nombre) {
	if(positifnegatif(nombre)) {
		printf("ce nombre est positif \n");
	}
	else {
		printf("ce nombre est négatif \n");
	}
}

int main(){
    int nombre;
    printf("Saisir un nombre : \n");
    scanf("%d", &nombre);
    verification(nombre);
}
