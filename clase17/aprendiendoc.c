#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char lastname[256];
	char name[256];
	char fullname[256];
	int year;
	
	printf("Garbage in string name %s\n", name);
	printf("Garbage in string lastname %s\n", lastname);
	
	strcpy(name, "Simon");
	strcpy(lastname, "El Bobito");
	
	printf("After initialization: %s %s\n", name, lastname);

	year = 1965;
	sprintf(fullname, "%s %s; Born %d", lastname, name, year);

	printf("Final string: %s\n", fullname);

	return 0;
}
