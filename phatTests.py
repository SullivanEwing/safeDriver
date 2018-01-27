
import numpy as np
import pandas as pd
import phat
from boundary_matrix import boundary_matrix


toy_data = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
data = pd.DataFrame(data = toy_data, index = ['A', 'B', 'C', 'D'], columns = ['a','b','c'])

complex = boundary_matrix(data)
print "filtered complex: "
print complex

boundary_matrix = phat.boundary_matrix(representation = phat.representations.vector_vector, columns = complex)

persistence_pairs = boundary_matrix.compute_persistence_pairs()
persistence_pairs.sort()

print persistence_pairs

print "There are {} persistence pairs: ".format(len(persistence_pairs))
for a,b in persistence_pairs:
	print "Birth: {}, Death: {}, lifespan: {}".format(a, b, b-a)


