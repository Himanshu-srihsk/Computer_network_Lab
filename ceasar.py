#12170032
#Himanshu

def encrypt(text,s):
	result=""
	for i in range(len(text)):
		char=text[i]
		if(char.isupper()):
			result+=chr((ord(char)+s-65)%26+65)
		else:
			result+=chr((ord(char)+s-97)%26+97)
	return result

text=raw_input("Enter text :")
s=3;
print "cipher :" +encrypt(text,s)

