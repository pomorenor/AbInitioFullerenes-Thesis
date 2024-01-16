#!/bin/bash 

PYTHONVER="python3"
LOWDINVER="lowdin2"

ORIGINALFILE="/home/pmorenor/Desktop/AbInitioFullerenes-Thesis/Code/NOCILevel/He3-C60-1S-NOCI.lowdin"
CHANGEGRID="/home/pmorenor/Desktop/AbInitioFullerenes-Thesis/Code/NOCILevel/change_lebedev_grid.py"
EXTRACTENERGY="/home/pmorenor/Desktop/AnInitioFullerenes-Thesis/code/NOCILevel/extract_lowdin_energy.py"
LINENUM="18"

grids=(26 38 50 74 86 110 146 170 194 230)

FILENAME="He3-C60-1S-NOCI"

#echo $FILENAME"_""2""_gridpoints"".lowdin"

for i in ${grids[@]}; do
	$PYTHONVER $CHANGEGRID $ORIGINALFILE $LINENUM $i
	NEWFILENAME=$FILENAME"_"$i"_gridpoints.lowdin"
	$LOWDINVER -i $NEWFILENAME 
	OUTPUTNAME=$FILENAME"_"$i"_gridpoints.out"	
	$PYTHONVER $EXTRACTENERGY $OUTPUTNAME
done 	





