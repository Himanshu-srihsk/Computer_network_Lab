#LZW DECODE
#12170032
#Himanshu

dictionary = {i:chr(i) for i in range(97,123)}
last = 257
arr = raw_input("Enter code : ").split(" ")
for i in range(len(arr)):
	arr[i]=int(arr[i])   
result = []
p = arr.pop(0)
result.append(dictionary[p])
for c in arr:
	if c in dictionary:
		entry = dictionary[c]
	        result.append(entry)
	dictionary[last] = dictionary[p] + entry[0]
	last += 1
	p = c 
print(''.join(result))
#print(dictionary)

"""
OUTPUT
Enter code : 97 98 257 259 260
abababab
"""
