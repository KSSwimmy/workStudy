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

# SOLUTION 2 -------------------------------------------------------------------------------

def sortedSquaredArray(array):
    # initiate a new array
	sortedArray = [0 for _ in array] # create a 0 for every space in the array
	# assign 2 pointers for the end
	smallerValueInx = 0
	# and the beganning of the array
	largerValueInx = len(array) - 1
	# loop through the array using reversed() because  range() because it's in ascending
	# order at lenth to get the entire length of the array
	for idx in reversed(range(len(array))):
		# assign the pointers at the arrays index so that it can be compared
		smallerValue = array[smallerValueInx]
		largerValue = array[largerValueInx]
		# we're going to compare what's bigger to the absolute value of the smallerValue to the bigger value
		if abs(smallerValue) > abs(largerValue):
			# then the sorted array at the index will be assigned to square the smallest value 
			sortedArray[idx] = smallerValue * smallerValue
			# then increment the starter pointer by one
			smallerValueInx += 1
		# otherwise 
		else:
			# then the sorted array at the index will be assigned to square the largest value
			sortedArray[idx] = largerValue * largerValue
			# then increment the end pointer by minus 1
			largerValueInx -= 1
	# return the new sorted array
	return sortedArray