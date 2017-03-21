def string_bits(str):
	'''
	Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

	string_bits('Hello') --> 'Hlo'
	string_bits('Hi') --> 'H'
	string_bits('Heeololeo') --> 'Hello'
	'''

 	result = ""
  	# Many ways to do this. This uses the standard loop of i on every char,
  	# and inside the loop skips the odd index values.
  	for i in range(len(str)):
    		if i % 2 == 0:
      			result = result + str[i]
  	return result




print "abcdefg" + ": " + string_bits("abcdefg")
print "abcdef" + ": " + string_bits("abcdef")
print "abcde" + ": " + string_bits("abcde")
print "abcd" + ": " + string_bits("abcd")
print "abc" + ": " + string_bits("abc")
print "ab" + ": " + string_bits("ab")
print "a" + ": " + string_bits("a")
print "<empty>" + ": " + string_bits("")
