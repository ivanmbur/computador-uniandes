#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void initial_condition(double *u, int n_points, double delta_x);
void copy(double *u_new, double *u_past, int n_x);
void update_u(double *u_future, double *u_present, double n_x, double r);
void print_u(double *u, double n_x, double delta_x);
int main(){


	double x_f = 1.0;
	int n_x = 80;
	double delta_x = 0.025;

	double delta_t = 0.001;
	int n_t = 300;
	double c = 1.0;
	double r = c * delta_t/delta_x;

	double *u_present = malloc(n_x*sizeof(double));
	double *u_future = malloc(n_x*sizeof(double));
	
	initial_condition(u_present, n_x, delta_x);
	/*print_u(u_past, n_x, delta_x);*/

	u_present[0] = 0.0;
	u_present[n_x-1] = 0.0;	
	
	int i;
	for(i=0;i<n_t;i++){
		update_u(u_future, u_present, n_x, r);
		copy(u_future, u_present, n_x);
	}
	print_u(u_present, n_x, delta_x);

	return 0;
}

void initial_condition(double *u, int n_x, double delta_x){
	
	int i;
	for(i=0;i<n_x;i++){
		double x = i*delta_x;
		if((x<1.25) && (x>0.75)){
			u[i] = 2;
		}
		else{
			u[i] = 0;
		}
	}
}

void copy(double *u_new, double *u_past, int n_x){
	int i;
	for(i=0;i<n_x;i++){
		u_past[i] = u_new[i];
	}
}

void update_u(double *u_future, double *u_present, double n_x, double r){
	int i;
	for(i=1;i<n_x-1;i++){
		u_future[i] = u_present[i] - (r*(u_present[i]-u_present[i-1]));
	}
}

void print_u(double *u, double n_x, double delta_x){
	int i;
	for(i=0;i<n_x;i++){
		printf("%f %f\n", i*delta_x ,u[i]);
	}
}

