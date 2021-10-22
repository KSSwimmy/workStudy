def sortedSquaredArray(array):
    # we're going to initialize an empty array
	sortedArray = [0 for x in array ]
	# loop through the range and length of the array
	for inx in range(len(array)):
		# assign the value at the array's index
		value = array[inx]
		# aassign the empty array at the array's index to square each value
		sortedArray[inx] = value * value 
	# come out of the loop and sort the new array using python's sort fuction
	sortedArray.sort()
	# return the new sorted array
	return sortedArray