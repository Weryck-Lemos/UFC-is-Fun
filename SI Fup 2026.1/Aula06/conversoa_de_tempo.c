#include <stdio.h>

int main()
{
	int segundos, minutos, horas;
	scanf("%d", &segundos);
	horas = segundos / 3600;
	segundos = segundos % 3600;
	minutos = segundos / 60;
	segundos = segundos % 60;
	printf("%d\n%d\n%d", horas, minutos, segundos);
}
