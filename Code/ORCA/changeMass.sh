#!/bin/bash

GEOMETRY="../../Coor_files/He3-C60-Ih-ANGS.XYZ"
STRING=" M 10E8"
NEWFILE="new_masses.xyz"

touch $NEWFILE

readarray -t lines < $GEOMETRY
for line in "${lines[@]}"; do
	echo ${line}$STRING
done > $NEWFILE 
