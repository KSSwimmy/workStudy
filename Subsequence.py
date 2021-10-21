def isValidSubsequence(array, sequence):
    # declear 2 trackers 
	# one to keep track of the initial array 
	initPointer = 0
	# the other to keep track of the sequence array
	subsPointer = 0
	# we will traverse through each array at the 
	# same time using a while loop
	# in the while loop we will compare the length of both 
	# arrays to the tracker 
	while initPointer < len(array) and subsPointer < len(sequence): 
		# if there is a match in the initial array 
		if array[initPointer] == sequence[subsPointer]: 
			# increment the subs pointer by 1
			subsPointer += 1
		# regardless if there's a match we'll continue to 
		# traverse throught the inital array. 
		# we will traverse through the initial array 
		initPointer += 1
	# return when we only have a valid sequence  
	return subsPointer == len(sequence)

	
	
    
