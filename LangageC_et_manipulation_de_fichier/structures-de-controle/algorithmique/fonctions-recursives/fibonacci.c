#include <stdio.h>

int main(){
	int nb_fonction[1000] = {1, 1};
	int max = 0;
	int resultat = 0;
	while (max < 2) {
	printf("veuillez choisir un maximum : \n");
	scanf("%d", &max);
	}
	for (int i = 2; i < max; i++) {
		resultat = nb_fonction[i -1] + nb_fonction[i -2];
		nb_fonction[i] = resultat;
	}
	for (int i = 0; i < max; i++) {
		printf("%d", nb_fonction[i]);
    		}	
	printf("\n");
}
