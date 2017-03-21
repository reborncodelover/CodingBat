def end_other(a,b):
	'''

	Given two strings, return True if either of the strings appears at the very end of the other string, 
	ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
	Note: s.lower() returns the lowercase version of a string.

	end_other('Hiabc', 'abc') --> True
	end_other('AbC', 'HiaBc') --> True
	end_other('abc', 'abXabc') --> True
	'''

	a = a.lower()
	b = b.lower()
	### This is one way to solve
	#a_len = len(a)
	#b_len = len(b)
	#if a[-b_len:] == b or b[-a_len:] == a:
		#return True
	#else:
		#return False
	## This another, maybe a better way to solve 
	return (b.endswith(a) or a.endswith(b))
