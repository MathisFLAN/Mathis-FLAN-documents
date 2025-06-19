#include <stdio.h>
#include <string.h>

int main() {
	char chaine[] = "bonjour, je suis Mathis";
	int nbCaracteres;
	printf("combien de caracteres voulez vous renvoyez ?\n");
	scanf("%d", &nbCaracteres);
	int fois = 0;
	while (fois != nbCaracteres && fois < strlen(chaine)) {
		printf("%c\n", chaine[fois]);
		fois = fois + 1;
	}
}
