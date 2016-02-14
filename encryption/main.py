from encryption import readKey, printK, generateRandomKey, firstKeyToKey, simpleEncrypt, blockEncrypt, randomBlockEncrypt
from decryption import simpleDecrypt



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
 
print simpleEncrypt(plaintext, K, key_len)

print "Encrypt Blocks of ", block_size, " :"
print blockEncrypt(plaintext, K, key_len, block_size)

print "-------------------------------"
print "Random Encrypt:"
ciphertext = randomBlockEncrypt(plaintext, K, key_len, block_size)
print ciphertext
print "Decrytpion:"
print simpleDecrypt(ciphertext, K, key_len)

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
