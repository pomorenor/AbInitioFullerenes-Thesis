#!/bin/bash

MASS=$1
GEOMETRY="../../Coor_files/He3-C60-Ih-ANGS.XYZ"
STRING="(Iso=$MASS)"
NEWFILE="new_masses.xyz"

touch $NEWFILE

sed "s/^\([^[:space:]]*\)/\1$STRING/" $GEOMETRY > $NEWFILE 
