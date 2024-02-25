#!/bin/bash

MASS=$1
GEOMETRY="../../Coor_files/C60_Ih-ANGS.xyz"
STRING="(Iso=$MASS)"
NEWFILE="new_masses.xyz"

touch $NEWFILE

sed "s/^\([^[:space:]]*\)/\1$STRING/" $GEOMETRY > $NEWFILE 
