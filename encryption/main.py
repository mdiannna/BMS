from encryption import encryptMessage, encryptBlocks, generateRandomKey, firstKeyToKey
from decryption import decryptMessage



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



# main
FK = [0] * 100000000
K = [0] * 100000000

first_key_len = 10
first_key = 123456389
plaintext = "----------"
block_size = 3

 
readKey(first_key,  FK, first_key)
printK(FK, first_key_len)
 
 
block_pos = 0
del_pos = 6
resultsK = firstKeyToKey(FK, first_key_len, block_pos, del_pos)
K = resultsK[0]
block_size = resultsK[1]
print "*************block block_size = ", block_size
key_len = first_key_len - FK[del_pos]-1 - FK[block_pos] - 1
 
print "---------------------new key: ----------"
printK(K, key_len)
 
print encryptMessage(plaintext, K, key_len)

print "Encrypt Blocks of ", block_size, " :"
print encryptBlocks(plaintext, K, key_len, block_size)



'''
# Random key test
# for i in range(0, 10):
rand_key = generateRandomKey(300)
print "Random key of length 300:", rand_key
# Big length key encryption test
key_len = 300
readKey(rand_key, K, key_len)
print "key_len:", key_len
# printK(K, key_len)

plaintext = "1111111111111111111111111111111111111111111111111111111111111111111111111"
print encryptMessage(plaintext, K, key_len)
'''
