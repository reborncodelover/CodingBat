def make_chocolate(small, big, goal):
	'''
	We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars 
	(5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. 
	Return -1 if it can't be done.

	make_chocolate(4, 1, 9) --> 4
	make_chocolate(4, 1, 10) --> -1
	make_chocolate(4, 1, 7) --> 2
	'''

	big_needed = goal / 5
	if big >= big_needed:
		small_needed = goal - big_needed * 5
		if small >= small_needed:
			return small_needed
		else:
			return -1
	else:
		small_needed = goal - big * 5
		if small >= small_needed:
			return small_needed
		else:
			return -1
