#!/bin/bash


#CHCOOR means change coordinates
#REENER means retrieve energy

PYTHONVER="python3"

DATA="/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Calculations/water2.lowdin"
CHCOOR="change_coordinates.py"
REENER="extract_lowdin_energy.py"

DX="0.1"
NUMSTEPS="20"


for ((ii = 0; ii < $NUMSTEPS; ++ii)); do
	$PYTHONVER $CHCOOR $DATA $DX
       		
done


