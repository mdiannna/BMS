import random
import string


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
		
		for i in range(0, K[key_pos]):
			extraCh = random.choice(string.ascii_letters)
			ciphertext = ciphertext + str(extraCh)

		ciphertext += plaintext[letter_pos]

		letter_pos += 1
		key_pos += 1

		if key_pos == key_len:
			key_pos = 0;

	for i in range(0, K[key_pos]):
		extraCh = random.choice(string.ascii_letters)
		ciphertext = ciphertext + str(extraCh)

	return ciphertext


def encryptBlocks(plaintext, K, key_len, block_size):
	letter_pos = 0
	plaintext_len = len(plaintext)
	ciphertext = ""

	while letter_pos < plaintext_len:
		block = ""
		for i in range(0, block_size):
			if letter_pos < plaintext_len:
				block = block + plaintext[letter_pos]
				letter_pos += 1
		cipher_block = encryptMessage(block, K, key_len)

		print cipher_block
		print("------------")
		ciphertext = ciphertext + cipher_block + "|"

	return ciphertext


def generateRandomKey(key_len):
	rand_key = 0
	for i in range(0, key_len):
		rand_key = rand_key*10 + random.randint(1, 9)
	return rand_key


def firstKeyToKey(first_key, key_len, block_pos, del_pos):
    block_size = 0
    new_key = [0]*key_len
    new_key_pos = 0
 
    for i in range(block_pos+1, first_key[block_pos+first_key[block_pos]]):
        block_size = block_size*10 + first_key[i]
 
    print "block size:",block_size
 
    for key_pos in range(0, key_len):
        if key_pos >= del_pos and key_pos <= del_pos + first_key[del_pos]:
            pass
        elif key_pos >= block_pos and key_pos <= block_pos + first_key[block_pos]:
            pass
        else:
            new_key[new_key_pos] = first_key[key_pos]
            new_key_pos += 1
 
    # new_key_len = 2
    return new_key #, new_key_len

# def dencryptMessage(ciphertext, key,  key_len):
# 	plaintext = ""
# 	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 	#Aici trebuie sa faci functia de decriptare
# 	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 	return plaintext

