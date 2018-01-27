#inputs: bdry_mx_in_prog, dimension, latest_simplex
#output:
#lists of simplices (given by their indices in bdry_mx_in_prog) of dimension "dimension" 
#which, together with last_simplex, form the boundary of a one-dimension-heigher simplex. the list includes last_simplex

from find_boundaries_recursive import find_boundaries_recursive

def simplex_check(complex): #recursive function
	print "starting simplex check"
	new_simplices = find_boundaries_recursive([[len(complex)-1]], [[[]]], complex)#, dimension, len(complex)). a list whose elements are of the form [dimension, [boundary]]
	print new_simplices
	if new_simplices:
		print "new_simplices: ", new_simplices
		for simplex in new_simplices:
			complex.append((complex[simplex[0]][0] + 1, simplex))
			print complex
	#for new_simplex in new_simplices:
	#	complex.append(new_)
	#	print complex
		simplex_check(complex)#, dimension+1)
	print "ending simplex check"
	return


