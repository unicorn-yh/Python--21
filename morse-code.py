# Python program to implement Morse Code Translator
morse_code_dict = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    'stop':'.-.-.-'
					}
def encrypt(st):
	code = ''
	for s in st:
		if st!=" ":
			code+=morse_code_dict[s]+" "
		else:
			code+=" "
	return code

def main():
	s = "GEEKS-FOR-GEEKS"
	print (encrypt(s.upper()))

# Executes the main function
if __name__ == '__main__':
	main()
