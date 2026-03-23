#include <stdio.h>

int main()
{
	double prova1, prova2, trabalho;
	scanf("%lf", &prova1);
	scanf("%lf", &prova2);
	scanf("%lf", &trabalho);
	double media = (5 * prova1 + 3 * prova2 + 2 * trabalho) / 10.0;
	printf("%f\n", media);
}
