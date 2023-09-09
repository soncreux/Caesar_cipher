def encrypt(text, shift):

	result = ""


	for  i in range(len(text)):

		char = text[i]

		if char==" ":
			result+=" "

		elif(char.isupper()):
			result += chr((ord(char) + shift - 64) % 26 + 64)
		else:
			result += chr((ord(char) + shift - 96) % 26 + 96)
	
	return result


text = input("Write your text: ")
str_shift = input("Write shift: ")
shift = int(str_shift)


print("Plain text: " + text)
print("Shift pattern: " + str(shift))
print("Cipher: " + encrypt(text, shift))
