#include <stdio.h>
int main(){
    int jour;
    printf("Saisir un chiffre entre 1 et 7 \n");
    scanf("%d", &jour);
    switch(jour){
    case 1 :
    	printf("Lundi \n");
    	break;
    case 2 :
    	printf("Mardi \n");
    	break;
    case 3 :
    	printf("Mercredi \n");
    	break;
    case 4 :
    	printf("Jeudi \n");
    	break;
    case 5 :
    	printf("Vendredi \n");
    	break;
    case 6 :
    	printf("Samedi \n");
    	break;
    case 7 :
    	printf("Dimanche \n");
    	break;
    default :
    	printf("ce n'est pas un jour ne la semaine");
    }
}
