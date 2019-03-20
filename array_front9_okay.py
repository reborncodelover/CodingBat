def array_front9(nums):
	'''
	Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
	The array length may be less than 4.

	array_front9([1, 2, 9, 3, 4]) --> True
	array_front9([1, 2, 3, 4, 9]) --> False
	array_front9([1, 2, 3, 4, 5]) --> False
	'''

	i = 0
	for num in nums:
		if num == 9:
			return True
		i += 1
		if i == 4:
			return False
	return False

# Alternate way 
'''
def array_front9(nums):
	look_for = 9
	if len(nums) < 4 and look_for in nums:
		return True
	elif look_for in nums[:4]:
		return True
	else:
		return False

'''

