#include <stdio.h>
int main(){
    char lettre;
    printf("Entrer un caractère: \n");
    scanf(" %c", &lettre);
    if(lettre == 'a' || lettre == 'e' || lettre == 'i' || lettre == 'o' || lettre == 'u' || lettre == 'y' || lettre == 'A' || lettre == 'E' || lettre == 'I' || lettre == 'O' || lettre == 'U' || lettre == 'Y')  {
    printf("%c est une voyelle. \n", lettre);
  }
    else {
      printf("%c est une consonne. \n", lettre);
  }
}
