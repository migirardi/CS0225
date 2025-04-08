#include <stdio.h>
int main() {
    int num1;
    int num2;
    printf("Inserisci il primo numero: ");
    scanf("%d", &num1);
    printf("Inserisci il secondo numero: ");
    scanf("%d", &num2);
    int molt = num1 * num2;
    printf("Risultato: %d\n", molt);
    return 0;
}