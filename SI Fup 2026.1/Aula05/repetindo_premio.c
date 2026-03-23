#include <stdio.h>

int main()
{
	double aposta1, aposta2, aposta3, premio;
	double ganho1, ganho2, ganho3, soma_apostas;
	scanf("%lf", &aposta1);
	scanf("%lf", &aposta2);
	scanf("%lf", &aposta3);
	scanf("%lf", &premio);
	soma_apostas = aposta1 + aposta2 + aposta3;
	ganho1 = premio * aposta1 / soma_apostas;
	ganho2 = premio * aposta2 / soma_apostas;
	ganho3 = premio * aposta3 / soma_apostas;
	printf("%f\n", ganho1);
	printf("%f\n", ganho2);
	printf("%f\n", ganho3);
}
