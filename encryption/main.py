from encryption import encryptMessage, readKey, encryptBlocks, generateRandomKey



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



K = [0] * 100000000

key_len = 4;
key = 1232
plaintext = "AAAAAAAAA"
block_size = 3

readKey(key, K, key_len)

print encryptMessage(plaintext, K, key_len)

print "Encrypt Blocks of 3:"
print encryptBlocks(plaintext, K, key_len, block_size)

# for i in range(0, 10):
rand_key = generateRandomKey(300)
print "Random key of length 300:", rand_key
key_len = 300
readKey(rand_key, K, key_len)
print "key_len:", key_len
printK(K, key_len)

plaintext = "1111111111111111111111111111111111111111111111111111111111111111111111111"
print encryptMessage(plaintext, K, key_len)
