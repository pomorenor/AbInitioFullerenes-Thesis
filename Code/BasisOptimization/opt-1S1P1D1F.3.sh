#!/bin/bash
#Optimiza el exponente de la funcion de onda nuclear

name=`echo $0| sed "s/.sh//"`

exp1S=`gawk ' ($1~/^X1$/ ){print $2} '  $1` 
exp1P=`gawk ' ($1~/^X2$/ ){print $2} '  $1` 
exp1D=`gawk ' ($1~/^X3$/ ){print $2} '  $1` 
exp1F=`gawk ' ($1~/^X4$/ ){print $2} '  $1` 

basis="HE-1S1P1D1F"

RX1=0.5390456966       
RY1=0.9788282225     
RZ1=-0.1383245163
RX2=-1.1024884940      
RY2=0.0000000000 
RZ2=0.2641072565
RX3=0.5390456966       
RY3=-0.9788282225       
RZ3=-0.1383245163

N=4

cat > $basis <<EOF 
O-HELIUM HEA3 (1S) BASIS TYPE: 2
$N
1 0 1
$exp1S 1.0
2 1 1
$exp1P 1.0
3 2 1
$exp1D 1.0
4 3 1
$exp1F 1.0

O-HELIUM HEB3 (1S) BASIS TYPE: 2
$N
1 0 1
$exp1S 1.0
2 1 1
$exp1P 1.0
3 2 1
$exp1D 1.0
4 3 1
$exp1F 1.0

O-HELIUM HES3 (1S) BASIS TYPE: 2
$N
1 0 1
$exp1S 1.0
2 1 1
$exp1P 1.0
3 2 1
$exp1D 1.0
4 3 1
$exp1F 1.0
EOF

cp $basis /home/linux-pohl-v2/Escritorio/LOWDIN2/openLOWDIN/lib/basis

cat > $name.lowdin <<EOF
GEOMETRY
HEA3  $basis   $RX1 $RY1 $RZ1 m=5497.888366
HEA3  $basis   $RX2 $RY2 $RZ2 m=5497.888366
HEB3  $basis   $RX3 $RY3 $RZ3 m=5497.888366
END GEOMETRY

TASKS
	method = "UHF"
END TASKS

CONTROL
	readCoefficients=.F.
	units="ANGS"
	totalEnergyTolerance=1E-10
	scfGlobalMaxIterations=10000
END CONTROL

EXTERPOTENTIAL
	HEA3   HE2C60-IH-1P
	HEB3   HE2C60-IH-1P
END EXTERPOTENTIAL

INTERPOTENTIAL
	HEA3 HEA3	HE2C60-IH-2P
	HEA3 HEB3	HE2C60-IH-2P
	HEB3 HEB3	HE2C60-IH-2P
END INTERPOTENTIAL

EOF

lowdin2 -i $name.lowdin -n 1 &> 2
