#include <stdio.h>

int main() {
    // Déclaration et affectation des variables caractères
    char lettre_c = 'c';
    char lettre_o = 'o';
    char lettre_C = 'C';
    char lettre_O = 'O';

    // Affichage des variables selon la forme demandée
    printf("lettre_c: '%c' %d\n", lettre_c, lettre_c);
    printf("lettre_o: '%c' %d\n", lettre_o, lettre_o);
    printf("lettre_C: '%c' %d\n", lettre_C, lettre_C);
    printf("lettre_O: '%c' %d\n", lettre_O, lettre_O);

    // Affichage de la soustraction entre les lettres
    printf("lettre_c - lettre_C = %d\n", lettre_c - lettre_C);
    printf("lettre_o - lettre_O = %d\n", lettre_o - lettre_O);

    /*
    Commentaire:
    - En ASCII, les lettres minuscules ont des codes plus grands que les majuscules.
    - Par exemple, 'c' (code 99) - 'C' (code 67) = 32
    - 'o' (111) - 'O' (79) = 32
    - Cette différence est donc logique et constante entre minuscules et majuscules en ASCII.
    */

    // Affectation de symboles spéciaux selon leur code ASCII (ou étendu)
    char grave_accent = 138;   // code ASCII étendu pour « grave accent » (selon table étendue)
    char percent_sign = 37;    // code ASCII standard pour '%'
    char euro_sign = 128;      // code ASCII étendu pour '€' (varie selon encoding)
    char copyright_sign = 184; // code ASCII étendu pour '©' (varie selon encoding)

    // Affichage des caractères spéciaux et leur code
    printf("Grave accent: '%c' %d\n", grave_accent, grave_accent);
    printf("Percent sign: '%c' %d\n", percent_sign, percent_sign);
    printf("Euro sign: '%c' %d\n", euro_sign, euro_sign);
    printf("Copyright sign: '%c' %d\n", copyright_sign, copyright_sign);

    /*
    Que se passe-t-il ? Est-ce normal ?
    - Les codes ASCII standards vont de 0 à 127.
    - Les valeurs supérieures (128+) font partie des codes étendus, qui dépendent de l'encodage (ex: ANSI, Windows-1252).
    - Donc, l'affichage et l'interprétation des symboles comme l'accent grave, l'euro ou copyright peuvent varier selon la console et l'encodage utilisé.
    - Parfois, on voit des caractères bizarres si l'encodage n'est pas adapté.
    - C'est normal dans ce contexte.
    */
}
