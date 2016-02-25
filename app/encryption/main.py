from encryption import readKey, printK, generateRandomKey, simpleEncrypt, blockEncrypt, randomBlockEncrypt, randomBlockEncryptV4
from decryption import simpleDecrypt2, randomBlockDecrypt, randomBlockDecryptV4

from keylib import readKey, printK, firstKeyToKey, keyTextSeparation




# First Key initialization - the initial key (containing block size parameter and masking the real key length)
FK = [0] * 100000000
# Real Key initialization
K = [0] * 100000000

# The length of the first key
first_key_len = 10
# The first key expressed as integer
first_key = 123456389
# The message to be encrypted
plaintext = "dAAAAAAAAAAAHH"
# ???????????????
# block_size = 3

# Function that transforms the key from integer to array of digits 
readKey(first_key,  FK, first_key_len)
 
# block_pos - block_size parameter position in the key 
block_pos = 0
# del_pos - a parameter that specifies how many of the following bits should be deleted from the key
del_pos = 6

# Function that transforms first(initial key) to real key used for the first block
resultsK = firstKeyToKey(FK, first_key_len, block_pos, del_pos)
# Real Key
K = resultsK[0]
# Obtaining block size
block_size = resultsK[1]

# Calculating real length of the key
key_len = first_key_len - FK[del_pos]-1 - FK[block_pos] - 1
 

# Encryption
print "-------------------------------"
print "Random Encryption V 4.2:"
ciphertext = randomBlockEncryptV4(plaintext, K, key_len, block_size)
print ciphertext

# Decryption
print "-------------Decryption:"
print ciphertext
print randomBlockDecryptV4(ciphertext, K, key_len, block_size)