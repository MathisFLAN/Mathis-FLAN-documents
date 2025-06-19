#include <stdio.h>
#include <string.h>

int main() {
    char chaine[] = "bonjour, je suis Mathis";
    int nbCaracteres;
    printf("combien de caracteres voulez vous renvoyez de la droite ?\n");
    scanf("%d", &nbCaracteres);
    int longueur = strlen(chaine);
    int debut = (nbCaracteres > longueur) ? 0 : longueur - nbCaracteres;
    for (int i = debut; i < longueur; i++) {
        printf("%c\n", chaine[i]);
    }
    return 0;
}
