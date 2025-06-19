#include <stdio.h>
int main(){
    int année;
    printf("Saisir une année \n");
    scanf("%d", &année);
    if(année % 4 == 0) {
    	if (année % 100 == 0) {
    		if (année % 400 == 0) {
    			printf("c'est une année bissextile \n");
    		}
    		else {
    			printf("ce n'est pas une année bissextile \n");
    		}
    	}
    	else {
    		printf("c'est une année bissextile \n");
    	}
    }
    else {
    	printf("ce n'est pas une année bissextile \n");
    }
}
