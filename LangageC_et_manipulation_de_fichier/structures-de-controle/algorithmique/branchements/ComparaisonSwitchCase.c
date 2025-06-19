#include <stdio.h>
int main(){
    int a;
    printf("Saisir un premier nombre: ");
    scanf("%d", &a);
    int b;
    printf("Saisir un deuxième nombre: ");
    scanf("%d", &b);
    int difference;
    int key;
    difference = a > b;
    switch(difference){
    case 1 :
    	printf("le chifre maximum est %d. \n", a);
    	break;
    case 0 :
    	printf("le chifre maximum est %d. \n", b);
    	break;
    }
}
