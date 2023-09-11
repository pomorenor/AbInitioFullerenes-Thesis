#!/bin/bash


#CHCOOR means change coordinates
#REENER means retrieve energy

PYTHONVER="python3"
LOWDINVER="lowdin2"

INPUT="/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Calculations/pes_test.lowdin"
OUTPUT="/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Calculations/pes_test.out"
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


