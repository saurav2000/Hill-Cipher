import sys
import sympy as sp

def textToMatrix(text_list):
	return sp.Matrix([[ord(x)-97 for x in s] for s in text_list]) 

def inverse(text_list):
	return textToMatrix(text_list).inv_mod(26)

def main():
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

	eng_text_inverse = inverse(top_eng_digraphs)

	for i in range(4):
		for j in range(4):
			if i==j:
				continue;
			key = (textToMatrix([top_freq[i], top_freq[j]]) * eng_text_inverse) % 26
			




if __name__ == '__main__':
	main()