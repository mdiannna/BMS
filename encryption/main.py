from encryption import readKey, printK, generateRandomKey, simpleEncrypt, blockEncrypt, randomBlockEncrypt, randomBlockEncryptV4
from decryption import simpleDecrypt2, randomBlockDecrypt, randomBlockDecryptV4

from keylib import readKey, printK, firstKeyToKey, keyTextSeparation




# main
FK = [0] * 100000000
K = [0] * 100000000

first_key_len = 10
first_key = 123456389
plaintext = "dAAAAAAAAAAAHH"
block_size = 3

 
readKey(first_key,  FK, first_key)
# printK(FK, first_key_len)
 
 
block_pos = 0
del_pos = 6
resultsK = firstKeyToKey(FK, first_key_len, block_pos, del_pos)
K = resultsK[0]
block_size = resultsK[1]
# print "*************block block_size = ", block_size
key_len = first_key_len - FK[del_pos]-1 - FK[block_pos] - 1
 
# print "---------------------new key: ----------"
# printK(K, key_len)
 
# print simpleEncrypt(plaintext, K, key_len)

# print "Encrypt Blocks of ", block_size, " :"
# print blockEncrypt(plaintext, K, key_len, block_size)

print "-------------------------------"
print "Random Encrypt:"
ciphertext = randomBlockEncryptV4(plaintext, K, key_len, block_size)
print ciphertext
# print "simple Decryption:"
# print simpleDecrypt2(ciphertext, K, key_len)

print "-------------Decryption:"
print randomBlockDecryptV4(ciphertext, K, key_len, block_size)


# readKey(keySeparation("------123", 6), K, 3)
# printK(K, key_len)