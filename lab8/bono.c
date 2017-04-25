#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float delta_n_step(float n, float lambda, float dt);
void single_decay(float N0, float lambda, float dt);

int main(){

	float N_0 = 100.0;
	float Lambda = 1.0/2.0;
	float Dt = 0.001;

	srand48(1);
	
	single_decay(N_0, Lambda, Dt);
		
	return 0;
}

float delta_n_step(float n, float lambda, float dt){
	
	float rand_num = drand48();
	if(rand_num < lambda*n*dt){
		return -1.0;
	} else {
		return 0.0;
	}
}
	
void single_decay(float N0, float lambda, float dt){

	int n_repeticiones = 1000;	
	float t_total = 5.0/lambda;
	int n_points = (int)t_total/dt;
	
	float *resultado = malloc(n_points*sizeof(float));
	
	FILE *out=fopen("data_rand.txt","w+");

	int m;
	for(m=0;m<n_repeticiones;m++)
	{
		int i;

		float t = 0.0;
		float n = N0;
	
		for(i=0;i<n_points;i++)
		{
	
			t += dt;
			float delta_n = delta_n_step(n, lambda, dt);
			n +=delta_n;
			resultado[i] += n;		
		}
	}
	
	float t = 0.0;
	
	int i;
	for(i=0;i<n_points;i++)
	{
		resultado[i] = resultado[i] / n_repeticiones;
		t += dt;
		fprintf(out, "%f %f\n", t, resultado[i]);
	}
	fclose(out);
}
