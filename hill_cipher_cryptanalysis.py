import sys
import sympy as sp

def inverse(text_list):
	key = sp.Matrix([[ord(x)-97 for x in s] for s in text_list])
	return key.inv_mod(26)

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

	most_freq = max(frequency_map, key = frequency_map.get)
	del frequency_map[most_freq]
	secmost_freq = max(frequency_map, key = frequency_map.get)




if __name__ == '__main__':
	main()