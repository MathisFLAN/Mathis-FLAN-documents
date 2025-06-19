#include <stdio.h>

int main () {
	int tableau[101];
	for(int i = 0; i < 101; i ++ ) {
		tableau[i] = i;
	}
	printf("%d \n", tableau[100]);
}
