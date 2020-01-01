#LZW ENCODE
#Himanshu
#12170032

string = raw_input("Enter input : ")
dictionary = {chr(i):i for i in range(97,123)}
last = 257
p = ""
result = []
for c in string:
	pc = p+c
	if pc in dictionary:
		p = pc
	else:
		result.append(dictionary[p])
		dictionary[pc] = last
		last += 1
		p = c
test=""
if p != '':
	#test.append(str(pi)+" "+ )
	result.append(dictionary[p])
print(result)

"""
OUTPUT
Enter input : abbabbabbabb
[97, 98, 98, 257, 259, 258, 260]
"""
