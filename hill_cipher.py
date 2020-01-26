import sys
import sympy as sp

def euclid(a, b):
	if(a==0):
		return (b, 0, 1)
	(g, x, y) = euclid(b%a, a)
	return (g, y - ((b//a) * x), x)

def mod_inverse(a, m):
	a = (a%m + m)%m
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

def textToMatrix(text_list):
	return sp.Matrix([[ord(x)-97 for x in s] for s in text_list])

def cryptionMain():
	# Reading lines
	file = open(sys.argv[1])
	lines = file.readlines()
	file.close()

	# Reading k and key and text and checking key's length
	k = int(lines[0][:-1])
	key_line = lines[1][:-1].strip().split(" ")
	text_lines = ''.join([x[:-1] for x in lines[2:]])
	text = ''.join([x for x in text_lines.strip() if 97<=ord(x)<=122])
	if(len(key_line)!=k*k):
		print("Key size improper")
		return

	# Checking determinant of key and computing key_mod_inverse & padding text
	key = sp.Matrix(k, k, [int(i) for i in key_line])
	det = key.det()
	det_inv = mod_inverse(det, 26)
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

def cryptanalysis():
	# Reading text
	file = open(sys.argv[1])
	cipher_text = file.read()[:-1]
	file.close()
	frequency_map = {}
	for i in range(0, len(cipher_text), 2):
		sub = cipher_text[i:i+2]
		if sub in frequency_map:
			frequency_map[sub]+=1
		else:
			frequency_map[sub]=1

	top_freq = sorted(frequency_map, key = frequency_map.get, reverse=True)[:4]
	top_eng_digraphs = ['th', 'he']

	eng_text_inverse = textToMatrix(top_eng_digraphs).inv_mod(26)

	for i in range(4):
		for j in range(4):
			if i==j:
				continue;
			key = (textToMatrix([top_freq[i], top_freq[j]]) * eng_text_inverse) % 26

def main():
	if(int(sys.argv[2])==2):
		cryptanalysis()
	else:
		cryptionMain()

if __name__ == '__main__':
	main()