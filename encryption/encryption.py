import random
import string


def readKey(nr, K, key_len):
	key_len = 0
	nr1 = nr

	while nr>0:
		nr = nr / 10
		key_len += 1

	i = key_len - 1

	while nr1>0:
		K[i] = nr1 % 10
		nr1 = nr1 / 10
		i -= 1



def encryptMessage(plaintext, K,  key_len):
	if not K:
		return "no key"
	ciphertext = ""
	letter_pos = 0
	key_pos = 0
	plaintext_len = len(plaintext)

	print " plaintext_len=", plaintext_len
	print "key_len=", key_len

	while letter_pos < plaintext_len:
		ciphertext += plaintext[letter_pos]

		for i in range(0, K[key_pos]):
			extraCh = random.choice(string.ascii_letters)
			ciphertext = ciphertext + str(extraCh)

		letter_pos += 1
		key_pos += 1

		if key_pos == key_len:
			key_pos = 0;

	return ciphertext


def encryptBlocks(plaintext, K, key_len, block_size):
	letter_pos = 0
	plaintext_len = len(plaintext)
	ciphertext = ""

	while letter_pos < plaintext_len:
		block = ""
		for i in range(0, block_size-1):
			if letter_pos < plaintext_len:
				block = block + plaintext[letter_pos]
				letter_pos += 1
		cipher_block = encryptMessage(block, K, key_len)

		print cipher_block
		print("------------")
		ciphertext = ciphertext + cipher_block + "|"

	return ciphertext



# def dencryptMessage(ciphertext, key,  key_len):
# 	plaintext = ""
# 	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 	#Aici trebuie sa faci functia de decriptare
# 	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 	return plaintext

