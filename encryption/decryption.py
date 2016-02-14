
def decryptMessage(plaintext, K,  key_len):
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
