def xyz_there(str):
	'''
	Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded 
	by a period (.). So "xxyz" counts but "x.xyz" does not.

	xyz_there('abcxyz') --> True
	xyz_there('abc.xyz') --> False
	xyz_there('xyz.abc') --> True
	'''
	count = 0
	prev_char = ""
	for i in range(len(str) - 2):
		substr = str[i:i+3]
		if substr == "xyz" and prev_char != ".":
			return True
		prev_char = str[i]
	return False
