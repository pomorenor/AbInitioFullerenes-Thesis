set heliums [atomselect top "element He"]
set num_helium_atoms [$heliums num]

for {set i 0} {$i < $num_helium_atoms} {incr i} {
	set unique_name "Helium_$i"
	set single_atom_selection [atomselect top "index $i"]
	$single_atom_selection set name $unique_name
}


