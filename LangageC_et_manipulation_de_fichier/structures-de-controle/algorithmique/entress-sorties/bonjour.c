#include <stdio.h>

int main() {
	char prenom[100];
	printf("Quel est votre prénom ? \n");
	scanf("%s", &prenom);
	printf("Bonjour %s \n", prenom);
}
