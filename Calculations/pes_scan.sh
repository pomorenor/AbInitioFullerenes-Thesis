#!/bin/bash


#CHCOOR means change coordinates
#REENER means retrieve energy

PYTHONVER="python3"
LOWDINVER="lowdin2"
OMIT_ERROR="2>/dev/null"

FILENAME="pestest"
IN=".lowdin"
OUT=".out"

INPUT="$FILENAME$IN"
OUTPUT="$FILENAME$OUT"


CHCOOR="change_coordinates.py"
REENER="extract_lowdin_energy.py"



DX="0.2"
DY="0.0"
DZ="0.0"
NUMSTEPS="10"

ALINE="6"
ELINE="4"

for ((ii = 0; ii < $NUMSTEPS; ++ii)); do
	$PYTHONVER $CHCOOR $INPUT $ALINE $ELINE $DX $DY $DZ
	$LOWDINVER -i $INPUT 
	ENERGY=$($PYTHONVER $REENER $OUTPUT)
	echo $ENERGY
done


