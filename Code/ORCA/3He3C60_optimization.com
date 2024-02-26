%mem=7GB

%nprocshared=8

%chk=pseudomolandfullereneopt

#P MP2/aug-cc-pVTZ Opt=CalcFC Units=Angstroms SCF=VeryTight

Geometry optimization of the fullerene plus pseudomolecule

0 1
C(Iso=1000000000)	-1.964333135699816	-1.4271715593359278	2.599270716529214
C(Iso=1000000000)	-2.9667066136952673	-0.6989045977556938	1.8335255161306296
C(Iso=1000000000)	-2.9667066136952673	0.6989045977556938	1.8335255161306296
C(Iso=1000000000)	-1.964333135699816	1.4271715593359278	2.599270716529214
C(Iso=1000000000)	-1.0023734838164011	0.7282669615802337	3.3341425013361317
C(Iso=1000000000)	-1.0023734838164011	-0.7282669615802337	3.3341425013361317
C(Iso=1000000000)	-3.2033348918213123	-1.4271715593359278	0.5945237568340694
C(Iso=1000000000)	-3.2033348918213123	1.4271715593359278	0.5945237568340694
C(Iso=1000000000)	-1.5814605349713464	2.605532256149058	1.8335255177181613
C(Iso=1000000000)	0.3828725949075199	1.1783606968131308	3.334142502923663
C(Iso=1000000000)	0.3828725949075199	-1.1783606968131308	3.334142502923663
C(Iso=1000000000)	-1.5814605349713464	-2.605532256149058	1.8335255177181613
C(Iso=1000000000)	0.7503084873109789	2.309212091177591	2.599270720233454
C(Iso=1000000000)	-0.25206499068447297	3.037479052228648	1.83352551983487
C(Iso=1000000000)	1.9893102476658935	2.309212091177591	1.8335255230099334
C(Iso=1000000000)	0.3674358908159273	3.4875727874615445	0.5945237615966644
C(Iso=1000000000)	-3.4304227594269867	-0.7282669615802337	-0.5945237658300822
C(Iso=1000000000)	-2.3472057321948676	2.605532256149058	0.594523757892424
C(Iso=1000000000)	1.7526819695398483	3.037479052228648	0.5945237637133733
C(Iso=1000000000)	-1.7526819695398483	3.037479052228648	-0.5945237637133733
C(Iso=1000000000)	-3.4304227594269867	0.7282669615802337	-0.5945237658300822
C(Iso=1000000000)	1.239001754004788	0.0	3.3341425039820174
C(Iso=1000000000)	0.7503084873109789	-2.309212091177591	2.599270720233454
C(Iso=1000000000)	-2.8109218784557637	-1.1783606968131308	-1.833525524068288
C(Iso=1000000000)	-0.25206499068447297	-3.037479052228648	1.83352551983487
C(Iso=1000000000)	-2.3472057321948676	-2.605532256149058	0.594523757892424
C(Iso=1000000000)	1.9893102476658935	-2.309212091177591	1.8335255230099334
C(Iso=1000000000)	0.3674358908159273	-3.4875727874615445	0.5945237615966644
C(Iso=1000000000)	-1.7526819695398483	-3.037479052228648	-0.5945237637133733
C(Iso=1000000000)	-0.3674358908159273	3.4875727874615445	-0.5945237615966644
C(Iso=1000000000)	2.428049277727294	0.0	2.59927072287934
C(Iso=1000000000)	-2.8109218784557637	1.1783606968131308	-1.833525524068288
C(Iso=1000000000)	1.7526819695398483	-3.037479052228648	0.5945237637133733
C(Iso=1000000000)	-0.3674358908159273	-3.4875727874615445	-0.5945237615966644
C(Iso=1000000000)	-1.9893102476658935	-2.309212091177591	-1.8335255230099334
C(Iso=1000000000)	-0.7503084873109789	-2.309212091177591	-2.599270720233454
C(Iso=1000000000)	-2.428049277727294	0.0	-2.59927072287934
C(Iso=1000000000)	-1.9893102476658935	2.309212091177591	-1.8335255230099334
C(Iso=1000000000)	-0.7503084873109789	2.309212091177591	-2.599270720233454
C(Iso=1000000000)	0.25206499068447297	-3.037479052228648	-1.83352551983487
C(Iso=1000000000)	1.5814605349713464	-2.605532256149058	-1.8335255177181613
C(Iso=1000000000)	1.964333135699816	-1.4271715593359278	-2.599270716529214
C(Iso=1000000000)	2.3472057321948676	-2.605532256149058	-0.594523757892424
C(Iso=1000000000)	2.8109218784557637	1.1783606968131308	1.833525524068288
C(Iso=1000000000)	-0.3828725949075199	1.1783606968131308	-3.334142502923663
C(Iso=1000000000)	2.8109218784557637	-1.1783606968131308	1.833525524068288
C(Iso=1000000000)	3.4304227594269867	-0.7282669615802337	0.5945237658300822
C(Iso=1000000000)	-1.239001754004788	0.0	-3.3341425039820174
C(Iso=1000000000)	0.25206499068447297	3.037479052228648	-1.83352551983487
C(Iso=1000000000)	1.5814605349713464	2.605532256149058	-1.8335255177181613
C(Iso=1000000000)	-0.3828725949075199	-1.1783606968131308	-3.334142502923663
C(Iso=1000000000)	1.0023734838164011	-0.7282669615802337	-3.3341425013361317
C(Iso=1000000000)	3.2033348918213123	-1.4271715593359278	-0.5945237568340694
C(Iso=1000000000)	2.9667066136952673	-0.6989045977556938	-1.8335255161306296
C(Iso=1000000000)	1.0023734838164011	0.7282669615802337	-3.3341425013361317
C(Iso=1000000000)	3.4304227594269867	0.7282669615802337	0.5945237658300822
C(Iso=1000000000)	2.3472057321948676	2.605532256149058	-0.594523757892424
C(Iso=1000000000)	1.964333135699816	1.4271715593359278	-2.599270716529214
C(Iso=1000000000)	3.2033348918213123	1.4271715593359278	-0.5945237568340694
C(Iso=1000000000)	2.9667066136952673	0.6989045977556938	-1.8335255161306296
He(Iso=3.016029)  0.5390456966        0.9788282225       -0.1383245163
He(Iso=3.016029)  -1.1024884940        0.0000000000        0.2641072565
He(Iso=3.016029)  0.5390456966       -0.9788282225       -0.1383245163



