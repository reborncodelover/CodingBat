def string_bits(str):
	'''
	Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

	string_bits('Hello') --> 'Hlo'
	string_bits('Hi') --> 'H'
	string_bits('Heeololeo') --> 'Hello'
	'''

	result = ""
	while True:
		if str:
			result = result + str[0]
			if len(str) >= 2:
				str = str[2:] #### Smart!!!
			else:
				return result
		else:
			return result



print "abcdefg" + ": " + string_bits("abcdefg")
print "abcdef" + ": " + string_bits("abcdef")
print "abcde" + ": " + string_bits("abcde")
print "abcd" + ": " + string_bits("abcd")
print "abc" + ": " + string_bits("abc")
print "ab" + ": " + string_bits("ab")
print "a" + ": " + string_bits("a")
print "<empty>" + ": " + string_bits("")
