import phat
from simplex_check import simplex_check


boundary_matrix_square = phat.boundary_matrix(representation = phat.representations.vector_vector)

complex = [ (0, []),

(0, []),
(0, []),
(1, [0,1]),
(1, [0,2]),
(1, [1,2]),
(0, []),
(1, [2,3]),
(1, [1,3]),
(2, [5,7,8]),
(2, [3,4,5]) ]

boundary_matrix_square.columns = complex

square_pairs = boundary_matrix_square.compute_persistence_pairs()

square_pairs.sort()

print("\nThere are %d persistence pairs: " % len(square_pairs))
for pair in square_pairs:
	print("Birth: %d, Death: %d" % pair)


simplex_check(complex, 1)

print complex