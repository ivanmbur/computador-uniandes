#include <stdio.h>
#include <stdlib.h>

int main()
{
	
	float E = 100.0;
	float A = 1.0;
	float L = 10.0;

	float n_cells = 30;
	float n_nodes = n_cells + 1;
	float *mesh = malloc(n_nodes*sizeof(float));

	int i;
	for(i=0;i<n_nodes;i++)
	{
		mesh[i] = i*L/n_cells;
		printf("%e\n", mesh[i]);
	}
}
