import numpy as np

def simplex_check(complex, dimension):
	if dimension == 1:
		edges = []
		for i in range(len(complex)):
			dimension, faces = complex[i]
			if dimension == 1:
				edges.append([i, faces])
		for edge in edges:
			start = edge[1][0] 
			end = edge[1][1]
			for new_edge in edges:
				if new_edge[1][0] == end:
					end = edge[1][1]
					for new_new_edge in edges:
						if new_new_edge[1][0] == end:
							end = edge[1][1]
							if start == end:
								complex.append('hat')



