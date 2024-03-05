#include <iostream>
#include "csv.h"
#include <vector>
#include <cmath>
#include <eigen3/Eigen/Dense>
#include <eigen3/Eigen/Eigenvalues>
#include <utility>


typedef std::vector<double> d_vector;
typedef std::vector<int> i_vector;

void list_degeneracies(int J, std::vector<i_vector> &list_of_states);
d_vector energies_oblate_top(d_vector RotConst, int J, std::vector<i_vector> &list_of_states);



int main(void)
{

	int J = 20;

	d_vector rotationalConstants = {2.93472, 2.91684, 1.46296};

	
	
	
	std::cout << "J" << "\t" << "k" << "\t"  << "m"  << "\t" << "E[cm-1]"  << std::endl;

	for(int ii = 0; ii < J+1; ii++){
		std::vector<i_vector> states;
		list_degeneracies(ii, states);
		d_vector energies = energies_oblate_top(rotationalConstants, ii, states);

		for(int ii = 0; ii < states.size(); ii++){
		std::cout << states[ii][0] << "\t" << states[ii][1] << "\t"  << states[ii][2]  << "\t" << energies[ii]  << std::endl;
		}

	}




	/*
	std::vector<i_vector> states;
	list_degeneracies(J, states);
	d_vector energies = energies_oblate_top(rotationalConstants, J, states);

	std::cout << "J" << "\t" << "k" << "\t"  << "m"  << "\t" << "E[cm-1]"  << std::endl;

	for(int ii = 0; ii < states.size(); ii++){
		std::cout << states[ii][0] << "\t" << states[ii][1] << "\t"  << states[ii][2]  << "\t" << energies[ii]  << std::endl;
	}

	*/
	


	return 0;
}


void list_degeneracies(int J, std::vector<i_vector> &list_of_states)
{
	for(int kk = -J; kk < J+1; kk++){
		for(int mm = -J; mm < J+1; mm++){
			i_vector state = {J, kk, mm};
			list_of_states.push_back(state);
		}
	}

}


d_vector energies_oblate_top(d_vector RotConst, int J, std::vector<i_vector> &list_of_states)
{

	d_vector energies;

	//remember that we have K = |k| in the energy calculation, so in reality we have less states, we need to purge them then 2J +1 values
	int n = 2*J + 1;

	//list_of_states.erase(list_of_states.begin(), list_of_states.end()+n);

	for(int ii = 0; ii < list_of_states.size(); ii++){
		energies.push_back(RotConst[1]*J*(J+1) + list_of_states[ii][1]*list_of_states[ii][1]*(RotConst[2] - RotConst[1]));
	}

	return energies;

}
