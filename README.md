# Hill-Cipher
## The file hill_cipher.py runs the encryption and decryption and is run by (Part 1)
> `python3 hill_cipher.py [INPUT_FILE_NAME] [MODE] [OUTPUT_FILE_NAME]`
- Where MODE is 0 for encryption and 1 for decryption
- Input file has the key size in the first line, key in row-major order in the second line and 3rd line has the text to be encrypted or decrypted

## Cryptanalysis (Part 2)
> `python3 hill_cipher.py [INPUT_FILE_NAME] [MODE] [OUTPUT_FILE_NAME]`
- The MODE will be 2 for cryptanalysis.
- The input file will contain the key size(2 or 3) in the first line and the encrypted text in the next line.
- The ouput file will contain the keys and the decrypted texts, for various combinations of digrams.
- The cryptanalysis is done using the top 2 digrams(th, he) and top 3 trigrams(the, and, ing) frequency.
- We check the top 25 frequencies of digrams and check all 25c2 combinations and compare it with th, he and check if the key is invertible, if invertible we print the key and the decrypted text.
- Out of all 25c2 combinations the th, he digrams are bound to appear somewhere. If they do not appear then the text size must be increased and the frequency should be checked.
- The same is done for trigrams as well if the key size is 3. All 25c3 combinations are checked against the, and, ing trigrams.
