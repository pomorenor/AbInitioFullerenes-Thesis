set heliums [atomselect top "element He"]
set helium_indices [$heliums get index]
set geomCenter {0.0 0.0 0.0}

foreach atom_index $helium_indices {
	set distance [measure vecdist $atom_index $geomCenter]
	puts "Atom: $atom_index Distance to point: $distance"
}

#for {set i 0} {$i < $num_helium_atoms} {incr i} {
#	set centerOfGeometry {0.0 0.0 0.0}
#	set atom_index [$heliums get index]
#	set distance [measure vecdist ]
	#set unique_name "Helium_$i"
	#set single_atom_selection [atomselect top "index $i"]
	#set single_atom_coordinates [$single_atom_selection get {x y z}]
	$single_atom_selection set name $unique_name
	#lappend helium_names  $single_atom_selection
}


