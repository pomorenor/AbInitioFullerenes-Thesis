#include <iostream>
#include "csv.h"
#include <vector>
#include <cmath>



typedef std::vector<double> positionVector;
typedef double InertiaTensor[3][3];


class Atom {
  public:
    positionVector r_i;
    double mass;
    double spin;
/*
    Atom(positionVector r_i, double mass, double spin){
      this->r_i = r_i;
      this->mass = mass;
      this->spin = spin;
    }
    */
    Atom(positionVector r_i, double mass){
      this->r_i = r_i;
      this->mass = mass;
    }
};

void computeInertiaTensor(std::vector<Atom> &allAtoms, InertiaTensor &I);




int main()
{
  int numAtoms = 3;
  positionVector  allXYZ[numAtoms]; 
  positionVector allR;
  std::vector<double> allMasses;
  std::vector<Atom> allAtoms;
  
  io::CSVReader<4, io::trim_chars<' '>, io::double_quote_escape<'	', '\"'>, io::no_comment> in("../Coor_files/csv_optimized3He3.csv");

  std::string X = "X";
  std::string Y = "Y";
  std::string Z = "Z";
  std::string MASS = "MASS";

  in.read_header(io::ignore_extra_column, X, Y, Z, MASS);
  double x, y, z, mass;

  while(in.read_row(x,y,z, mass)){
            allR.push_back(x);
            allR.push_back(y);
            allR.push_back(z);
	    allMasses.push_back(mass);
  }

  //Now create the position vector for the atoms


  // allR is fine, the problem comes ahead

  
  for(int ii = 0; ii < numAtoms; ii++){
    for (int jj = 0; jj <3;  jj++){
      int kk = 3*ii + jj;
      allXYZ[ii].push_back(allR[kk]);
    }
  }

  
  // Now we initialize the atoms

  int ii = 0;
  while(ii < numAtoms){
    allAtoms.push_back(Atom(allXYZ[ii],allMasses[ii]));
    ii++;
  }


  InertiaTensor I;

  computeInertiaTensor(allAtoms, I);

  for(int ii = 0; ii < 3; ii++){
    for(int jj = 0; jj < 3; jj++){
      std::cout << I[ii][jj] << std::endl;
    }
  }

  return 0;
}



void computeInertiaTensor(std::vector<Atom> &allAtoms, InertiaTensor &I)
{
  double Temp_01 = 0.0;
  double Temp_02 = 0.0;
  double Temp_12 = 0.0;
    
  for(int ii = 0; ii < 3; ii++){
    I[0][0] += allAtoms[ii].mass*(std::pow(allAtoms[ii].r_i[1],2) +std::pow(allAtoms[ii].r_i[2],2));
    I[1][1] += allAtoms[ii].mass*(std::pow(allAtoms[ii].r_i[0],2) +std::pow(allAtoms[ii].r_i[2],2));
    I[2][2] += allAtoms[ii].mass*(std::pow(allAtoms[ii].r_i[0],2) +std::pow(allAtoms[ii].r_i[1],2));

    Temp_01 += allAtoms[ii].mass*allAtoms[ii].r_i[0]*allAtoms[ii].r_i[1];
    Temp_02 += allAtoms[ii].mass*allAtoms[ii].r_i[0]*allAtoms[ii].r_i[2];
    Temp_12 += allAtoms[ii].mass*allAtoms[ii].r_i[1]*allAtoms[ii].r_i[2];
  }

  I[0][1] += -Temp_01;
  I[0][2] += -Temp_02;
  I[1][2] += -Temp_12;

  I[1][0] = I[0][1];
  I[2][0] = I[2][0];
  I[2][1] = I[1][2];
 
}
