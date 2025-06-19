#include <stdio.h>

void classement(int tableau[], int retenu, int taille){
	for(int j = 0; j < taille - 1; j++) {
		if (tableau[j] > tableau[j+1]) {
			retenu = tableau[j];
			tableau[j] = tableau[j+1];
			tableau[j+1] = retenu;
		}
	}
}

int main(){
	int retenu = 0;
	int taille = int taille = sizeof(tableau) / sizeof(tableau[0]);
	int tableau[10] = {6, 1, 0, 9, 7, 2, 3, 8, 5, 4};
	
	for(int h = 0; h < taille; h++) {
		classement(tableau, retenu, taille);
	}
	
	printf("Contenu du tableau :\n");
	for(int i = 0; i < taille; i++) {
	        printf("%d ", tableau[i]);
    }
}
