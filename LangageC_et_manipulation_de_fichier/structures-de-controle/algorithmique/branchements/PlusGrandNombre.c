#include <stdio.h>

int main(){
	int a;
	printf("Saisir un premier nombre: ");
	scanf("%d", &a);
	int b;
	printf("Saisir un deuxième nombre: ");
	scanf("%d", &b);
	int c;
	printf("Saisir un deuxième nombre: ");
	scanf("%d", &c);
	if(a > b && a > c){
		printf("le plus grand est le premier nombre\n");
	} else if (b > c && b > a){
		printf("le plus grand est le deuxième nombre\n");
	} else {
		printf("le plus grand est le troisième nombre\n");
	}
}
