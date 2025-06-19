#include <stdio.h>
int main(){
    int a;
    printf("Saisir un premier nombre: ");
    scanf("%d", &a);
    int b;
    printf("Saisir un deuxième nombre: ");
    scanf("%d", &b);
    int difference;
    difference = a > b;
    switch(difference){
    case 1 :
    	printf("le chiffre maximum est %d. \n", a);
    	break;
    case 0 :
    	printf("les chiffres sont égaux. \n");
    	break;
    default :
    	printf("le chiffre maximum est %d. \n", b);
    	}
    }
