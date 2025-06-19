#include <stdio.h>

void classement(int tableau[], int tableaufinal[], int taille, int emplacement) {
    int retenu = 1000;
    for(int j = 0; j < taille; j++) {
        if (tableau[j] < retenu) {
            retenu = tableau[j];
        }
    }
    for (int k = 0; k < taille; k++) {
        if (tableau[k] == retenu) {
            tableau[k] = 30;
        }
    }
    tableaufinal[emplacement] = retenu;
}

int main() {
    int emplacement = 0;
    int tableau[10] = {16, 11, 10, 9, 7, 12, 3, 18, 5, 4};
    int taille = sizeof(tableau) / sizeof(tableau[0]);
    int tableaufinal[sizeof(tableau) / sizeof(tableau[0])] = {0};

    for(int h = 0; h < taille; h++) {
        classement(tableau, tableaufinal, taille, emplacement);
        emplacement++;
    }

    printf("Contenu du tableau final:\n");
    for(int i = 0; i < taille; i++) {
        printf("%d ", tableaufinal[i]);
    }
}
