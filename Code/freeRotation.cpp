#include <iostream>
#include "csv.h"
#include <vector>
#include <cmath>
#include <eigen3/Eigen/Dense>
#include <eigen3/Eigen/Eigenvalues>
#include <utility>

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



void computeInertiaTensor(std::vector<Atom> &allAtoms, Eigen::Matrix3d &I);
void computeRotationalConstants(Eigen::Matrix3Xcd &D, std::vector<double> &rotConstVect);
void organizeMatrix(Eigen::Matrix3Xcd &D, Eigen::Matrix3Xcd &I);

double computeKappa(std::vector<double> &rotConstVect);


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

  // We convert to SI



  Eigen::Matrix3d I = Eigen::Matrix3d::Zero();

  computeInertiaTensor(allAtoms, I);

  //std::cout << I << std::endl;

  // Now we will diagonalize the matrix

  Eigen::EigenSolver<Eigen::Matrix3d> PrincipalAxis(I);
  Eigen::Matrix3Xcd D = PrincipalAxis.eigenvalues().asDiagonal();
  //Eigen::VectorXcd v = PrincipalAxis.eigenvectors().col(0);

  // Now we want to sort the eigenalues so we can follow the Ia<Ib<Ic convention

  Eigen::Matrix3Xcd sortedInertiaTensor = Eigen::Matrix3Xcd::Zero(3, 3);
  organizeMatrix(D, sortedInertiaTensor);





  std::vector<double> rotConstVect = {0.0,0.0,0.0};
  computeRotationalConstants(sortedInertiaTensor,rotConstVect);


  for(int ii = 0; ii < 3; ii++){
    std::cout << rotConstVect[ii] << std::endl;
  }

  std::cout << computeKappa(rotConstVect) << std::endl;


  return 0;
}



void computeInertiaTensor(std::vector<Atom> &allAtoms, Eigen::Matrix3d &I)
{
  double Temp_01 = 0.0;
  double Temp_02 = 0.0;
  double Temp_12 = 0.0;

  for(int ii = 0; ii < 3; ii++){
    I(0,0) += allAtoms[ii].mass*(std::pow(allAtoms[ii].r_i[1],2) +std::pow(allAtoms[ii].r_i[2],2));
    I(1,1) += allAtoms[ii].mass*(std::pow(allAtoms[ii].r_i[0],2) +std::pow(allAtoms[ii].r_i[2],2));
    I(2,2) += allAtoms[ii].mass*(std::pow(allAtoms[ii].r_i[0],2) +std::pow(allAtoms[ii].r_i[1],2));

    Temp_01 += allAtoms[ii].mass*allAtoms[ii].r_i[0]*allAtoms[ii].r_i[1];
    Temp_02 += allAtoms[ii].mass*allAtoms[ii].r_i[0]*allAtoms[ii].r_i[2];
    Temp_12 += allAtoms[ii].mass*allAtoms[ii].r_i[1]*allAtoms[ii].r_i[2];
  }

  I(0,1) += -Temp_01;
  I(0,2) += -Temp_02;
  I(1,2) += -Temp_12;

  I(1,0) = I(0,1);
  I(2,0) = I(0,2);
  I(2,1) = I(1,2);

}



void computeRotationalConstants(Eigen::Matrix3Xcd &D, std::vector<double> &rotConstVect)
{
  double m_e = 9.109E-31;
  double M = 1E-10;
  double hbar = 1.054571817E-34;
  double c = 29979245800;

  // c is in cm/s

  for(int ii = 0; ii < 3; ii++){
    rotConstVect[ii] = hbar/(4*M_PI*c*D(ii,ii).real()*m_e*M*M);
  }

}

void organizeMatrix(Eigen::Matrix3Xcd &D, Eigen::Matrix3Xcd &I)
{
  std::vector<double> eigenvalues;
  for(int ii = 0; ii < 3; ii++){
    eigenvalues.push_back(D(ii,ii).real());
  }
  std::sort(eigenvalues.begin(), eigenvalues.end());

  for(int ii = 0; ii < 3; ii++){
    I(ii,ii) = eigenvalues[ii];
  }

  for(int ii = 0; ii < 3; ii++){
    for(int jj = 0; jj < 3; jj++){
      std::cout << I(ii,jj) << std::endl;
    }
  }
}


double computeKappa(std::vector<double> &rotConstVect)
{
  double kappa = (2*rotConstVect[1] - rotConstVect[0] - rotConstVect[2])/(rotConstVect[1]-rotConstVect[2]);
  return kappa;
}
