#include <stdio.h>

void triParSelection(int tableau[], int taille) {
    for (int i = 0; i < taille - 1; i++) {
        int indiceMin = i;

        for (int j = i + 1; j < taille; j++) {
            if (tableau[j] < tableau[indiceMin]) {
                indiceMin = j;
            }
        }

        // Échange si nécessaire
        if (indiceMin != i) {
            int temp = tableau[i];
            tableau[i] = tableau[indiceMin];
            tableau[indiceMin] = temp;
        }
    }
}

void afficherTableau(int tableau[], int taille) {
    for (int i = 0; i < taille; i++) {
        printf("%d ", tableau[i]);
    }
    printf("\n");
}

int main() {
    int tableau[] = {64, 25, 12, 22, 11};
    int taille = sizeof(tableau) / sizeof(tableau[0]);

    printf("Avant le tri par sélection :\n");
    afficherTableau(tableau, taille);

    triParSelection(tableau, taille);

    printf("Après le tri par sélection :\n");
    afficherTableau(tableau, taille);

    return 0;
}
