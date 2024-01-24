#include <iostream>
#include <cmath>


double minDis(double r, double theta);
double maxDis(double r, double alpha);

int main(){

	double r = 1.13;

	for (double ii = M_PI/2; ii < M_PI; ii += 0.01){
		std::cout << ii << "\t" << minDis(r, ii) << "\t" << maxDis(r, ii) << std::endl;
	}

	return 0;	
}

double minDis(double r, double theta)
{
	double md = std::sqrt(r*r + r*r - 2*r*r*std::cos(theta));
	return md;
}


double maxDis(double r, double theta)
{
	double alpha = M_PI - theta;
	double maxp = 2*r*std::sin(alpha);
	return maxp;
}
