
def simpleDecrypt(plaintext, K,  key_len):
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
	plaintext = simpleDecrypt(block, K, key_len)
	return plaintext, cipherblock_len


def randomBlockDecrypt(ciphertext, K,  key_len, block_size):
	
	letter_pos = 0
	ciphertext_len = len(ciphertext)
	plaintext = ""
	cipherblock_len = 0

	print "Block size =", block_size
	print "Key len =", key_len

	first_block_decrypt_res = firstBlockDecrypt(ciphertext, K,  key_len, block_size)
	first_block_plaintext = first_block_decrypt_res[0]

	letter_pos = first_block_decrypt_res[1]
	cipherblock_len += block_size + key_len
	i = 0
	cipher_pos = first_block_decrypt_res[1]
	while cipher_pos < block_size + 1 + key_len + first_block_decrypt_res[1]:
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
		plaintext += simpleDecrypt(block, K, key_len)
		
	
	# 	readKey(generateRandomKey(key_len), rand_key, key_len)
	# 	block = block + keyToText(rand_key, key_len)
	# 	cipher_block = simpleEncrypt(block, K, key_len)

	# 	print block
	# 	print cipher_block
	# 	print("------------")
	# 	ciphertext = ciphertext + cipher_block + "|"

	return first_block_plaintext + plaintext


