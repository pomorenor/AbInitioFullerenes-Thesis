#include <iostream>
#include <vector>
#include <fstream>
#include <string> 


typedef std::vector<double> vec;

vec triangle_center(vec atom_1, vec atom_2, vec atom_3);
vec distance(vec atom_1, vec atom_2);



int main(void)
{

  vec  atom_1(3), atom_2(3), atom_3(3);
 
  std::ifstream file("3He3_D3.txt");
  
  for(int i = 0; i < 3; ++i)
  {
    file >> atom_1[i] >> atom_2[i] >> atom_3[i];
  }  

  vec Center = triangle_center(atom_1, atom_2, atom_3);
  
  for(int ii = 0; ii < 3; ii++){
    std::cout << Center[ii] << "\n" << std::endl;
  }
 
  
  return 0;
}

vec triangle_center(vec atom_1, vec atom_2, vec atom_3)
{
  vec Tcenter = {0.0, 0.0, 0.0};

  for(int ii = 0; ii < 3; ii++){
    Tcenter[ii] = (atom_1[ii] + atom_2[ii] + atom_3[ii])/3.0;
  }

  return Tcenter;
}

vec distance(vec atom_1, vec atom_2){

  double distance = 0.0;
  vec distance_vector(3);

  for(int ii = 0 ii < 3; ii++){

    distance += (atom_1[ii] - atom_2[ii])**2;
    distance_vector[ii] = atom_1[ii] - atom_2[ii];
  }



}
