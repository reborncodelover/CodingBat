def close_far(a, b, c):
	'''
	Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), 
	while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes 
	the absolute value of a number.

	close_far(1, 2, 10) --> True
	close_far(1, 2, 3) --> False
	close_far(4, 1, 3) --> True
	'''
	if is_close(a,b):
		if is_close(c,a) == False and is_close(c,b) == False:
			return True
		else:
			return False
	elif is_close(a,c):
		if is_close(c,b) == False:
			return True
		else:
			return False
	return False

def is_close(a,b):
	if abs(a-b) <= 1:
		return True
	else:
		return False
