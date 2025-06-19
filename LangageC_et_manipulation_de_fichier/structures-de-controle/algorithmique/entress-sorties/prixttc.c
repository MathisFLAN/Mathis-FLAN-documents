#include <stdio.h>

int main() {
    float prixHT;
    int quantite;
    float tauxTVA;
    float prixTTC;
    printf("Entrez le prix HT d'un article : ");
    scanf("%f", &prixHT);
    printf("Entrez le nombre d'articles : ");
    scanf("%d", &quantite);
    printf("Entrez le taux de TVA (en pourcentage, par exemple 20 pour 20%%) : ");
    scanf("%f", &tauxTVA);
    prixTTC = prixHT * quantite * (1 + tauxTVA / 100);
    printf("Prix HT unitaire       : %.2f €\n", prixHT);
    printf("Quantité               : %d\n", quantite);
    printf("Taux de TVA            : %.2f %%\n", tauxTVA);
    printf("Prix total TTC         : %.2f €\n", prixTTC);
}

