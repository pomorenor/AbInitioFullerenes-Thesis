#!/bin/bash


#CHCOOR means change coordinates
#REENER means retrieve energy
#CDIS means compute distance

PYTHONVER="python3"
LOWDINVER="lowdin2"


FILENAME="pestest"
IN=".lowdin"
OUT=".out"

INPUT="$FILENAME$IN"
OUTPUT="$FILENAME$OUT"


CHCOOR="/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Code/change_coordinates.py"
REENER="/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Code/extract_lowdin_energy.py"
CDIS="/home/linux-pohl-v2/Escritorio/AbInitioFullerenes-Thesis/Code/compute_distance.py"


DX="0.2"
DY="0.0"
DZ="0.0"
NUMSTEPS="30"

ALINE="6"
ALINEE="7"
ELINE="4"

for ((ii = 0; ii < $NUMSTEPS; ++ii)); do
	$PYTHONVER $CHCOOR $INPUT $ALINE $ELINE $DX $DY $DZ
	$LOWDINVER -i $INPUT 
	ENERGY=$($PYTHONVER $REENER $OUTPUT)
	DISTANCE=$($PYTHONVER $CDIS $INPUT $ALINE $ALINEE)
	echo $DISTANCE $ENERGY
done


