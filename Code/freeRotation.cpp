#include <iostream>
#include "csv.h"
#include <vector>



typedef std::vector<double> positionVector;

struct Atom {
  positionVector r_i;
};

int main()
{
  io::CSVReader<3, io::trim_chars<' '>, io::double_quote_escape<' ', '\"'>, io::no_comment> in("../Coor_files/csv_optimized3He3.csv");

  std::string X = "X";
  std::string Y = "Y";
  std::string Z = "Z";

  in.read_header(io::ignore_extra_column, X, Y, Z);
  double x;
  double y;
  double z;

  // Here would be anything about the number of atoms

  



  while(in.read_row(x,y,z)){
            std::cout << x << "\t" << y << "\t" << z << std::endl;
  }

  return 0;
}
