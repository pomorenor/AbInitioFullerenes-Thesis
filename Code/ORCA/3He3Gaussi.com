%mem=2GB

%nprocshared=5

%chk=pseudomolecule

#p MP2/aug-cc-pVTZ Opt=CalcFC Freq=(ReadIsotopes,vibrot) Units=Angstroms SCF=VeryTight Output=Pickett 

Computation of normal modes and frequencies free pseudomolecule

0 1
He(Iso=3.0)  0.5390456966        0.9788282225       -0.1383245163 
He(Iso=3.0)  -1.1024884940        0.0000000000        0.2641072565 
He(Iso=3.0)  0.5390456966       -0.9788282225       -0.1383245163 

















