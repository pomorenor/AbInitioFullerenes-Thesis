#!/bin/bash


#CHCOOR means change coordinates
#REENER means retrieve energy

PYTHONVER="python3"

DATA="/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Calculations/pes_test.lowdin"
CHCOOR="change_coordinates.py"
REENER="extract_lowdin_energy.py"

DX="0.1"
DY="0.0"
DZ="0.0"
NUMSTEPS="20"

ALINE="6"
ELINE="4"

for ((ii = 0; ii < $NUMSTEPS; ++ii)); do
	$PYTHONVER $CHCOOR $DATA $ALINE $ELINE $DX $DY $DZ
       		
done


