#!/bin/bash 

PYTHONVER="python3"
LOWDINVER="lowdin2"

ORIGINALFILE="He3-C60-1S-NOCI.lowdin"
CHANGEGRID="change_lebedev_grid.py"
EXTRACTENERGY="ELE.py"
LINENUM="18"

grids=(26 50 74 86 110 146 170 194 230 266 302)

FILENAME="He3-C60-1S-NOCI"

#echo $FILENAME"_""2""_gridpoints"".lowdin"

REGISTERFILE="GRIDENERGIES.txt"

for i in ${grids[@]}; do
	$PYTHONVER $CHANGEGRID $ORIGINALFILE $LINENUM $i
	$LOWDINVER -i $FILENAME"_"$i"_gridpoints.lowdin" 	
	$PYTHONVER $EXTRACTENERGY $FILENAME"_"$i"_gridpoints.out" $REGISTERFILE $i
done 	





