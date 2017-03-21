def sum13(nums):
	'''
	Return the sum of the numbers in the array, returning 0 for an empty array. 
	Except the number 13 is very unlucky, so it does not count and numbers that come 
	immediately after a 13 also do not count.

	sum13([1, 2, 2, 1]) --> 6
	sum13([1, 1]) --> 2
	sum13([1, 2, 2, 1, 13]) --> 6
	'''
	sum = 0
	last_num = None
	for num in range(len(nums)):
		if last_num != 13:
			if nums[num] != 13:
				sum += nums[num]
		last_num = nums[num]
	return sum
