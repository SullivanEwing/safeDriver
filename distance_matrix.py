#input "point cloud data" dataframe with every cell containing a floating point number

#output sorted pd series with pairs of points as indices, and edge length in each cell

import math
import numpy as np
import pandas as pd

def distance(point1, point2):
	dimension = len(point1)
	if dimension != len(point2):
		raise "Points are not from the same space"
	result = 0
	k = 0
	while k < dimension:
		result += (point1[k]-point2[k])**2
		k += 1
	return result**(0.5)


def distance_matrix(df):

	index = []
	i = 0
	while i < len(df):
		j = i
		while j < len(df):
			index.append((df.index[i], df.index[j]))

			#result[(df.index[i], df.index[j])] = distance(df.iloc[i], df.iloc[j])
			j += 1
		i += 1
	result = pd.Series(index = index)

	for (a,b) in index:
		result[(a,b)] = distance(df.loc[a], df.loc[b])


	return result.sort_values()

toy_data_array = np.array([[1,2,3], [4, 5, 6], [7,8,9], [10,11,12]])
toy_data = pd.DataFrame(data = toy_data_array, index = ['a', 'b', 'c', 'd'], columns = ['A', 'B', 'C'])

print toy_data
print distance_matrix(toy_data)

#print distance(toy_data.loc['a'],toy_data.loc['b'])