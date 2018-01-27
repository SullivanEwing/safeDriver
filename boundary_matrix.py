#input: points, a "point cloud data" dataframe
#output: boundary matrix list whose elements are [dimension, [boundary]], in the order in which they are
#added to the filtration as epsilon is increased.

import math
import numpy as np
import pandas as pd
from edge_distances import edge_distances
from simplex_check import simplex_check
#from find_boundaries_recursive import get_boundary_matches

def boundary_matrix(points):
	result = []

	#add all the points
	i = 0
	n = len(points)
	while i < n:
		result.append((0, []))
		#print result
		i += 1

	#get the edge lengths
	edges = edge_distances(points)
	
	#main loop to add the edges and higher simplices
	i = 0 #index in edges
	while i < (n * (n-1))/2: 
		(start, end) = edges.index[i]
		result.append((1, [start, end])) #add next edge
		#print result
		#print "about to run simplex_check"
		simplex_check(result) #add any necessary higher simplices
		i += 1
	return result



#thing = get_boundary_matches([1,1],[4, 7], f)
#print thing




