import sys
import sympy as sp

def euclid(a, b):
	if(a==0):
		return (b, 0, 1)
	(g, x, y) = euclid(b%a, a)
	return (g, y - ((b//a) * x), x)

def inverse(a, m):
	(g, x, y) = euclid(a, m)
	if(g!=1):
		return -1
	return (x%m + m)%m

def cryption(text, key, k):
	l = []	
	for i in range(0, len(text), k):
		res = ((key * sp.Matrix(text[i:i+k])) % 26)
		l+= [x+97 for x in res]
	return list(l)

def main():
	# Reading lines
	file = open(sys.argv[1])
	lines = file.readlines()
	file.close()

	# Reading k and key and text and checking key's length
	k = int(lines[0][:-1])
	key_line = lines[1][:-1].strip().split(" ")
	text = lines[2][:-1].strip().replace(" ","")
	if(len(key_line)!=k*k):
		print("Key size improper")
		return

	# Checking determinant of key and computing key_inverse & padding text
	key = sp.Matrix(k, k, [int(i) for i in key_line])
	det = key.det()
	det_inv = inverse(det, 26)
	if(det_inv==-1):
		print("Key det improper")
		return
	key_inv = key.inv_mod(26)
	padding = 0 if len(text)%k==0 else (k - len(text)%k)
	for i in range(padding):
		text+= "x"
	text_ascii = sp.Matrix([ord(a)-97 for a in text])

	#Computing final result and printing to file
	res_text = cryption(text_ascii, key if int(sys.argv[2])==0 else key_inv, k) 
	final_text = str(''.join(chr(i) for i in res_text))
	file = open(sys.argv[3], "w")
	print(final_text, file=file)
	file.close()

if __name__ == '__main__':
	main()