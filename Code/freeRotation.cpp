#include <iostream>
#include "csv.h"
#include <vector>



typedef std::vector<double> positionVector;

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

  for(int ii = 0; ii < numAtoms; ii++){
    for (int jj = 0; jj <3;  jj++){
      int kk = ii + jj;
      allXYZ[ii].push_back(allR[kk]);
    }
  }

  
  // Now we initialize the atoms

  int ii = 0;
  while(ii < numAtoms){
    allAtoms.push_back(Atom(allXYZ[ii],allMasses[ii]));
    ii++;
  }





  return 0;
}
