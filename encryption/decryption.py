from keylib import readKey, keyTextSeparation, printK
from copy import copy



def simpleDecrypt1(plaintext, K,  key_len):
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
			# extraCh = random.choice(string.ascii_letters)
			# ciphertext = ciphertext + str(extraCh)
			letter_pos += 1

		if letter_pos < plaintext_len:
			ciphertext += plaintext[letter_pos]

		letter_pos += 1
		key_pos += 1

		if key_pos == key_len:
			key_pos = 0;

	# for i in range(0, K[key_pos]):
	# 	extraCh = random.choice(string.ascii_letters)
	# 	ciphertext = ciphertext + str(extraCh)

	return ciphertext


def simpleDecrypt2(ciphertext, key,  key_len):
	plaintext = ""
	key_pos = 0;
	cipher_pos = 0;
	ciphertext_len = len(ciphertext)
	while cipher_pos<ciphertext_len :
		cipher_pos = cipher_pos  +  key[key_pos]

		if cipher_pos <ciphertext_len :
			plaintext = plaintext + ciphertext[cipher_pos]
		key_pos += 1
		cipher_pos += 1
		if key_pos == key_len :
			key_pos = 0

	return plaintext



def firstBlockDecrypt(ciphertext, K,  key_len, block_size):
	block = ""

	cipherblock_len = key_len
	i = 0
	cipher_pos = 0
	while cipher_pos < key_len + 1:
		if i == key_len:
			i=0
		cipherblock_len += K[i]
		cipher_pos += 1
		i += 1

	for i in range(0, cipherblock_len):
		block += ciphertext[i]
	plaintext = simpleDecrypt2(block, K, key_len)
	return plaintext, cipherblock_len


def randomBlockDecrypt(ciphertext, K,  key_len, block_size):
	
	letter_pos = 0
	ciphertext_len = len(ciphertext)
	plaintext = ""	
	cipherblock_len = 0
	prev_rand_key = [0] * key_len
	rand_key = [0] * key_len

	print "Block size =", block_size
	print "Key len =", key_len

	first_block_decrypt_res = firstBlockDecrypt(ciphertext, K,  key_len, block_size)
	first_block_plaintext = first_block_decrypt_res[0]
	print "+++++first_block_plaintext", first_block_plaintext

	readKey(keySeparation(first_block_plaintext, 0), rand_key, key_len)
	print "+++++rand_key=", rand_key

	first_cipherblock_len = first_block_decrypt_res[1]


	letter_pos = first_cipherblock_len
	cipherblock_len += block_size + key_len
	i = 0
	cipher_pos = first_cipherblock_len
	while cipher_pos < block_size + 1 + key_len + first_cipherblock_len:
		if i == key_len:
			i=0
		cipherblock_len += K[i]
		cipher_pos += 1
		i += 1

	print "cipherblock_len = ", cipherblock_len

	while letter_pos < ciphertext_len:
		block = ""
		for i in range(0, cipherblock_len):	
			if letter_pos < ciphertext_len:
				block = block + ciphertext[letter_pos]
			letter_pos += 1
		print "+++++block_cipher=", block
		block_plaintext = simpleDecrypt1(block, K, key_len)
		plaintext += block_plaintext
		print "+++++block_plaintext=", block_plaintext
	
	# 	readKey(generateRandomKey(key_len), rand_key, key_len)
	# 	block = block + keyToText(rand_key, key_len)
	# 	cipher_block = simpleEncrypt(block, K, key_len)

	# 	print block
	# 	print cipher_block
	# 	print("------------")
	# 	ciphertext = ciphertext + cipher_block + "|"

	return first_block_plaintext + plaintext



def calcCipherblockLen(block_size, key, key_len):
	cipherblock_len = block_size + key_len
	key_pos = 0
	for i in range(0, block_size + key_len + 1):
		if key_pos == key_len:
			key_pos = 0
		cipherblock_len += key[key_pos]
		key_pos +=1
	return cipherblock_len


def randomBlockDecryptV4(ciphertext, K,  key_len, block_size):
	
	letter_pos = 0
	ciphertext_len = len(ciphertext)
	plaintext = ""	
	cipherblock_len = 0
	prev_rand_key = [0] * key_len
	rand_key = [0] * key_len
	# last block reached flag
	last = False

	print "Block size =", block_size
	print "Key len =", key_len

	first_block_decrypt_res = firstBlockDecrypt(ciphertext, K,  key_len, block_size)
	first_block_plaintext = first_block_decrypt_res[0]
	print "+++++first_block_plaintext", first_block_plaintext


	key_text_separation = keyTextSeparation(first_block_plaintext, 0)
	separated_key =  key_text_separation[0]
	readKey(separated_key , rand_key, key_len)


	print "+++++rand_key=", rand_key

	first_cipherblock_len = first_block_decrypt_res[1]


	letter_pos = first_cipherblock_len

	

	while letter_pos < ciphertext_len:
		prev_rand_key = copy(rand_key)
		cipherblock_len = calcCipherblockLen(block_size, prev_rand_key, key_len)
		# test if the last block(incomplete) reached
		if cipherblock_len > ciphertext_len - letter_pos:
			cipherblock_len = copy(ciphertext_len - letter_pos)
			last = True
		print "cipherblock_len = ", cipherblock_len
		block = ""

		for i in range(0, cipherblock_len):	
			if letter_pos < ciphertext_len:
				block = block + ciphertext[letter_pos]
			letter_pos += 1
		print "+++++block_cipher=", block
		block_plaintext = simpleDecrypt2(block, prev_rand_key, key_len)

		if last:
			key_text_separation = keyTextSeparation(block_plaintext, len(block_plaintext)-key_len)
		else:
			key_text_separation = keyTextSeparation(block_plaintext, block_size)
		separated_key =  key_text_separation[0]
		separated_plaintext = key_text_separation[1]

		plaintext += separated_plaintext
		print "+++++block_plaintext=", block_plaintext
		# print "+++++prev_rand_key=", prev_rand_key
		
		readKey(separated_key, rand_key, key_len)

		
	
	# 	readKey(generateRandomKey(key_len), rand_key, key_len)
	# 	block = block + keyToText(rand_key, key_len)
	# 	cipher_block = simpleEncrypt(block, K, key_len)

	# 	print block
	# 	print cipher_block
	# 	print("------------")
	# 	ciphertext = ciphertext + cipher_block + "|"

	return plaintext

