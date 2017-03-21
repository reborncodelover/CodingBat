def centered_average(nums):
	'''
	Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
	except ignoring the largest and smallest values in the array. If there are multiple copies of the 
	smallest value, ignore just one copy, and likewise for the largest value. Use int division to 
	produce the final average. You may assume that the array is length 3 or more.

	centered_average([1, 2, 3, 4, 100]) --> 3
	centered_average([1, 1, 5, 5, 10, 8, 7]) --> 5
	centered_average([-10, -4, -2, -4, -2, 0]) --> -3
	'''
	min_value = min(nums)
	max_value = max(nums)
	skip_min, skip_max = True, True
	elem_count, sum = 0, 0
	for num in nums:
		if (num == min_value and skip_min):
			skip_min = False
		elif (num == max_value and skip_max):
			skip_max = False
		else:
			elem_count +=1
			sum += num
	if elem_count:
		return sum / elem_count
	else:
		return 0

