def twoNumberSum(array, targetSum):

	# sort the array 
	array.sort()
	# assign the the left pointer at the beginning of the
	# array and the right at the end 
	leftP = 0
	rightP = len(array) - 1
	# we'll establish a while loop stating that 
	# the left pointer should always be less than 
	# the right because it's a sorted array 
	while leftP < rightP:
		# establish a formula to solve: each pointer 
		# in the array will add up to see if it is the targetSum
		currentSum = array[leftP] + array[rightP]
		# if the tartgetSum is equal to currentSum 
		if currentSum == targetSum:
			# return the numbers that the right and 
			# left points are currently located
			return [array[leftP], array[rightP]]
		# if else continue to compare the currentSum to the targetSum 
		# by traversing through the array using the right pointer 
		elif currentSum < targetSum:
			# incrementing the left pointer to the right +1 
			leftP += 1
		# if else contine to compare the currentSum to the targetSum 
		# by traversing through the array using the left pointer
		elif currentSum > targetSum:
			# decrementing the right pointer to the left -1
			rightP -= 1
	# return an empty array
	return []	
	