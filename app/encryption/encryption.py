import random
import string
from copy import copy




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


def printK(K, key_len):
	for i in range(0, key_len):
		print K[i]


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
 
    
    return new_key, block_size


def simpleEncrypt(plaintext, K,  key_len):
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



def blockEncrypt(plaintext, K, key_len, block_size):
	letter_pos = 0
	plaintext_len = len(plaintext)
	ciphertext = ""

	while letter_pos < plaintext_len:
		block = ""
		for i in range(0, block_size):
			if letter_pos < plaintext_len:
				block = block + plaintext[letter_pos]
				letter_pos += 1
		cipher_block = simpleEncrypt(block, K, key_len)

		print cipher_block
		print("------------")
		ciphertext = ciphertext + cipher_block + "|"

	return ciphertext


def generateRandomKey(key_len):
	rand_key = 0
	for i in range(0, key_len):
		rand_key = rand_key*10 + random.randint(1, 9)
	return rand_key


def keyToText(rand_key, key_len):
	text = ""
	for i in range(0, key_len):
		text += str(rand_key[i])
	return text

# V 4.0
def randomBlockEncrypt(plaintext, K,  key_len, block_size):
	
	print "Key plaintext:", plaintext

	letter_pos = 0
	plaintext_len = len(plaintext)
	ciphertext = ""

	rand_key = [0] * 10000000
	# generate and encrypt first block - just a random key 
	readKey(generateRandomKey(key_len), rand_key, key_len)
	block = keyToText(rand_key, key_len)
	
	ciphertext += simpleEncrypt(block, K, key_len)

	print "First block:", block

	while letter_pos < plaintext_len:
		block = ""
		# rand_key = [0] * 100000000
		for i in range(0, block_size):
			if letter_pos < plaintext_len:
				block = block + plaintext[letter_pos]
				letter_pos += 1

		readKey(generateRandomKey(key_len), rand_key, key_len)
		block = block + keyToText(rand_key, key_len)
		cipher_block = simpleEncrypt(block, K, key_len)

		print block
		print cipher_block
		print("------------")
		ciphertext = ciphertext + cipher_block #+ "|"

	return ciphertext




# def dencryptMessage(ciphertext, key,  key_len):
# 	plaintext = ""
# 	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 	#Aici trebuie sa faci functia de decriptare
# 	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 	return plaintext



def randomBlockEncryptV4(plaintext, K,  key_len, block_size):
	if not K:
		return "no key"
	print "Key plaintext:", plaintext

	letter_pos = 0
	plaintext_len = len(plaintext)
	ciphertext = ""
	rand_key = [0]*key_len
	

	# generate and encrypt first block - just a random key 
	readKey(generateRandomKey(key_len), rand_key, key_len)
	block = keyToText(rand_key, key_len)

	prev_rand_key = rand_key
	
	ciphertext += simpleEncrypt(block, K, key_len)

	print "First block:", block

	while letter_pos < plaintext_len:
		block = ""
		K = copy(prev_rand_key)
		printK(K, key_len)
		# rand_key = [0] * 100000000
		for i in range(0, block_size):
			if letter_pos < plaintext_len:
				block = block + plaintext[letter_pos]
				letter_pos += 1

		readKey(generateRandomKey(key_len), rand_key, key_len)
		block = block + keyToText(rand_key, key_len)
		cipher_block = simpleEncrypt(block, K, key_len)

		prev_rand_key = copy(rand_key)

		print block
		print cipher_block
		print("------------")
		ciphertext = ciphertext + cipher_block #+ "|"

	print ""
	print "_______----_______----____Encryption Result:________------"
	return ciphertext
