
import copy


def find_boundaries_recursive(possible_boundaries, used_indices, complex):

	test_boundaries = copy.deepcopy(possible_boundaries)
	test_used_indices = copy.deepcopy(used_indices)

	if test_boundaries == []:
		print "sentinel case empty set"
		return []

	print "test_boundaries: ", test_boundaries

	if test_boundaries[0] and len(test_boundaries[0]) == complex[test_boundaries[0][0]][0] + 2:
		print "found a boundary and it's", test_boundaries
		return test_boundaries

	else:
		print "test used indices: " , test_used_indices
		new_boundaries = []
		new_indices = []
		i = 0
		while i < len(test_boundaries):
			print "i = ", i
			print "test_used_indices[i]: ", test_used_indices[i]
			indices = get_next_indices(test_used_indices[i])
			print "use indices {} for possible boundary {}: ".format(indices, test_boundaries[i]) 
			matches, found_indices = get_boundary_matches(test_boundaries[i], indices, complex)

			if matches:
				print "matches:", matches
				k = 0
				while k < len(indices): #add the indices we just used to indices_tested
					print "inside of if matches, test_used_indices is {} and indices is {}".format(test_used_indices, indices)
					print "so test_used_indices[i][k] is {}".format(test_used_indices[i][k])
					test_used_indices[i][k].append(indices[k])
					print "now test_used_indices is ", test_used_indices
					k +=1

			j = 0	
			while j < len(matches):
				new_boundaries.append(test_boundaries[i] + [matches[j]])
				new_indices.append(copy.deepcopy(test_used_indices[i]) + [found_indices[j]])

				j += 1

			i +=1

		return find_boundaries_recursive(new_boundaries, new_indices, complex)



##### CHECK THIS #####
def get_next_indices(used_indices): #used indices is a list. each item corresponds to one simplex's boundary.
#it is itself a list telling which boundary elements have been used already on that simplex
	if used_indices == [[]]:
		return [0]

	result = []
	for index_list in used_indices:
		j = 0
		while j in index_list:
			j += 1
		result.append(j)
	return result


def get_boundary_matches(possible_boundary, indices, complex):

	#build list of the facets we are looking to match
	test = []
	i = 0
	while i < len(possible_boundary):
		test.append(complex[possible_boundary[i]][1][indices[i]]) #build list of facets to test
		i += 1
	print "facets to test: ", test

	#check each simplex in the complex to see if it matches all the facets in test
	matches = []
	found_indices = []
	i = 0
	while i < len(complex)-1:
		print "checking simplex {} for boundary matches".format(i)
		temp_indices = []
		is_match = True #initializing at True means this will break if possible_boundary is empty
		for facet in test:
			if facet not in complex[i][1]: #if you don't have one of the test facets, you're not a match!
				is_match = False
			else:
				temp_indices.append(complex[i][1].index(facet)) #keep track of where you found each facet
		if is_match:											#save the matches and their found_indices
			found_indices.append(temp_indices)
			matches.append(i)
		i += 1
		

	return matches, found_indices



