def make_bricks(small, big, goal):
	'''
	We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) 
	and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given 
	bricks. This is a little harder than it looks and can be done without any loops. 

	make_bricks(3, 1, 8) --> True
	make_bricks(3, 1, 9) --> False
	make_bricks(3, 2, 10) --> True
	'''

	big_needed = goal / 5
	small_needed = goal % 5
	if big >= big_needed:
		# we have enough big bricks needed, but we need enough small bricks too
		return small >= small_needed 
	else:
		# we have insufficient big bricks, so we need enough small bricks to make up the difference too	
		small_needed = goal - big * 5
		return small >= small_needed
