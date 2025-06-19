#include <stdio.h>

// Fonction pour effectuer le tri à bulle
void triABulle(int tableau[], int taille) {
    for (int i = 0; i < taille - 1; i++) {
        for (int j = 0; j < taille - i - 1; j++) {
            if (tableau[j] > tableau[j + 1]) {
                // Échange des éléments
                int temp = tableau[j];
                tableau[j] = tableau[j + 1];
                tableau[j + 1] = temp;
            }
        }
    }
}

// Fonction pour afficher le tableau
void afficherTableau(int tableau[], int taille) {
    for (int i = 0; i < taille; i++) {
        printf("%d ", tableau[i]);
    }
    printf("\n");
}

int main() {
    int tableau[] = {64, 25, 12, 22, 11};
    int taille = sizeof(tableau) / sizeof(tableau[0]);

    printf("Tableau avant le tri :\n");
    afficherTableau(tableau, taille);

    triABulle(tableau, taille);

    printf("Tableau après le tri :\n");
    afficherTableau(tableau, taille);

    return 0;
}
