#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>

#define MAX_LIGNE 1024

// Vérifie si le fichier existe et si l'utilisateur a les droits nécessaires
int verifier_fichier(const char *nom_fichier) {
    struct stat buffer;
    
    // Vérifie l'existence du fichier
    if (stat(nom_fichier, &buffer) != 0) {
        perror("Erreur : Le fichier n'existe pas ou n'est pas accessible");
        return 0;
    }

    // Vérifie les permissions en lecture
    if (access(nom_fichier, R_OK) != 0) {
        perror("Erreur : Permission de lecture refusée");
        return 0;
    }

    return 1;
}

// Fonction qui oiuvre le fichier
FILE *ouvrir_fichier(const char *nom_fichier) {
    FILE *fichier = fopen(nom_fichier, "r");
    if (!fichier) {
        perror("Erreur lors de l'ouverture du fichier");
        return NULL;
    }
    return fichier;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage : %s <nom_du_fichier>\n", argv[0]);
        return EXIT_FAILURE;
    }

    const char *nom_fichier = argv[1];

    // Vérification de l'existence et des permissions du fichier
    if (!verifier_fichier(nom_fichier)) {
        return EXIT_FAILURE;
    }

    // Ouverture du fichier
    FILE *fichier = ouvrir_fichier(nom_fichier);
    if (!fichier) {
        return EXIT_FAILURE;
    }

    char ligne[MAX_LIGNE];

    // Boucle de lecture ligne par ligne
    while (fgets(ligne, sizeof(ligne), fichier)) {

        if ((ligne[0] == 'k' || ligne[0] == 'K') && (strchr(ligne, 'a') != NULL || strchr(ligne, 'A') != NULL)) {
            printf("%s\n", ligne);  // Affiche la ligne lue
        }
    }

    // Fermeture du fichier
    fclose(fichier);

    return EXIT_SUCCESS;
}
