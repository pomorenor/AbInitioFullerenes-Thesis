#!/bin/bash
#Optimiza el exponente de la funcion de onda nuclear

name=`echo $0| sed "s/.sh//"`

RX1=`gawk ' ($1~/^X1$/ ){print $2} '  $1` 
RY1=`gawk ' ($1~/^X2$/ ){print $2} '  $1` 
RZ1=`gawk ' ($1~/^X3$/ ){print $2} '  $1` 
RX2=`gawk ' ($1~/^X4$/ ){print $2} '  $1` 
RY2=`gawk ' ($1~/^X5$/ ){print $2} '  $1` 
RZ2=`gawk ' ($1~/^X6$/ ){print $2} '  $1` 
RX3=`gawk ' ($1~/^X7$/ ){print $2} '  $1` 
RY3=`gawk ' ($1~/^X8$/ ){print $2} '  $1` 
RZ3=`gawk ' ($1~/^X9$/ ){print $2} '  $1` 

exp1S=1000000
N=1

cat > HE-INF <<EOF 
O-HELIUM HEA3 (1S) BASIS TYPE: 2
$N
1 0 1
$exp1S 1.0

O-HELIUM HEB3 (1S) BASIS TYPE: 2
$N
1 0 1
$exp1S 1.0

O-HELIUM HES3 (1S) BASIS TYPE: 2
$N
1 0 1
$exp1S 1.0
EOF

cp HE-INF ~/.lowdin2/lib/basis/

cat > $name.lowdin <<EOF
GEOMETRY
HEA3  HE-INF   $RX1 $RY1 $RZ1 m=10000000000000
HEA3  HE-INF   $RX2 $RY2 $RZ2 m=10000000000000
HEB3  HE-INF   $RX3 $RY3 $RZ3 m=10000000000000
END GEOMETRY

TASKS
	method = "UHF"
END TASKS

CONTROL
	readCoefficients=.F.
	units="BOHRS"
	totalEnergyTolerance=1E-10
	scfGlobalMaxIterations=1000
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

