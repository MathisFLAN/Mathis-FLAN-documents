#include <stdio.h>

int est_pair(int nombre) {
	return nombre % 2 == 0;
}

void pair_ou_impair(int nombre) {
	if(est_pair(nombre)) {
		printf("Ce nombre est pair\n");
	}
	else {
		printf("Ce nombre est impair\n");
	}
}

int main(){
    int nombre;
    printf("Saisir une chiffre \n");
    scanf("%d", &nombre);
    pair_ou_impair(nombre);
}
