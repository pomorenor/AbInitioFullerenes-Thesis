%mem=48GB

%nprocshared=24

%Chk=twobasissetopt.chk
%rwf=frequenciesfp

#P MP2 gen Freq=SelectNormalModes Units=Angstroms Geom=AllCheck Guess=Read

C 0
6-311G
********
He 0
cc-pVTZ
********

atoms=He
notatoms=C












