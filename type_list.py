#l = ['magical unicorns', 19, 'hello', 98.98, 'world']
#l = [2,3,1,7,4,12]
#l = ["magical", "unicorns"]


s = "" 			# new string
strcount = 0	# number of strings in list
su = 0			# running sum
intcount = 0	# number of integers in list
floatcount = 0	# number of floats in list

#loop through the list, check the type, and do something with it
for x in l:
	if type(x) is str:
		s += (x + " ")
		strcount += 1
	elif type(x) is int:
		su += x
		intcount += 1
	elif type(x) is float:
		su += x
		floatcount += 1


#prints out the type of list and the string or sum
if strcount != 0 and intcount == 0 and floatcount == 0:
	listtype = "string"
	print "The list you entered is of " + listtype + " type"
	print "String: " + s
elif strcount == 0 and intcount != 0 and floatcount == 0:
	listtype = "integer"
	print "The list you entered is of " + listtype + " type"
	print "Sum: ", su
elif strcount == 0 and intcount == 0 and floatcount != 0:
	listtype = "float"
	print "The list you entered is of " + listtype + " type"
	print "Sum: ", su
elif strcount != 0 or intcount != 0 or floatcount != 0:
	listtype = "mixed"
	print "The list you entered is of " + listtype + " type"
	if len(s) != 0:
		print "String: " + s
	print "Sum: ", su