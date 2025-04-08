#include <stdio.h>
float main(){
    float a;
    float b;
    printf("Inserisci il primo numero: ");
    scanf("%f", &a);
    printf("Inserisci il secondo numero: ");
    scanf("%f", &b);
    float somma = a + b;
    printf("La somma sarà: %f\n", somma);
    float media = somma / 2;
    printf("La media sarà: %f", media);
    return 0;
}