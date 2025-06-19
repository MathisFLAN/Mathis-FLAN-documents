#include <stdio.h>

void triParInsertion(int tableau[], int taille) {
    for (int i = 1; i < taille; i++) {
        int cle = tableau[i];
        int j = i - 1;

        // Déplacement des éléments supérieurs à cle
        while (j >= 0 && tableau[j] > cle) {
            tableau[j + 1] = tableau[j];
            j--;
        }
        tableau[j + 1] = cle;
    }
}

void afficherTableau(int tableau[], int taille) {
    for (int i = 0; i < taille; i++) {
        printf("%d ", tableau[i]);
    }
    printf("\n");
}

int main() {
    int tableau[] = {29, 10, 14, 37, 13};
    int taille = sizeof(tableau) / sizeof(tableau[0]);

    printf("Avant le tri par insertion :\n");
    afficherTableau(tableau, taille);

    triParInsertion(tableau, taille);

    printf("Après le tri par insertion :\n");
    afficherTableau(tableau, taille);

    return 0;
}
