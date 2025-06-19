#include <stdio.h>
#include <string.h>

int main() {
	char chaine1[] = "Hello";
	printf("chaine 1 : %s\n", chaine1);
	char chaine2[] = "Hello";
	
	if (strcmp(chaine1,chaine2) == 0) {
		printf("ces 2 chaines de caracteres sont authentique. \n");
	}
	else {
		printf("ces 2 chaines de caracteres sont différentes. \n");
	}
}
