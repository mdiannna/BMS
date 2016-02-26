from encryption import readKey, printK, generateRandomKey, simpleEncrypt, blockEncrypt, randomBlockEncrypt, randomBlockEncryptV4
from decryption import simpleDecrypt2, randomBlockDecrypt, randomBlockDecryptV4

from keylib import readKey, printK, firstKeyToKey, keyTextSeparation

import timeit
# from Crypto import Random


# print "Random:"
# print Random.new().read(19)


# First Key initialization - the initial key (containing block size parameter and masking the real key length)
FK = [0] * 10000000
# Real Key initialization
K = [0] * 10000000

# The length of the first key
first_key_len = 10
# The first key expressed as integer
first_key = 173456389
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


def encrypt(plaintext):
	# Encryption
	# print "-------------------------------"
	# print "Random Encryption V 4.2:"
	ciphertext = randomBlockEncryptV4(plaintext, K, key_len, block_size)
	# print ciphertext
	return ciphertext

	

def decrypt(ciphertext):
	# Decryption
	# print "-------------Decryption:"
	# print ciphertext
	plaintext = randomBlockDecryptV4(ciphertext, K, key_len, block_size)
	# print plaintext
	return plaintext


def test(plaintext, iterations):

		start_time = timeit.default_timer()
		ciphertext = encrypt(plaintext)
		enc_elapsed = timeit.default_timer() - start_time
		print("--- Encryption execution time: %s seconds ---" % enc_elapsed)
		

		start_time = timeit.default_timer()
		decrypt(ciphertext)
		dec_elapsed = timeit.default_timer() - start_time
		print("--- Decryption execution time: %s seconds ---" % dec_elapsed)

		return enc_elapsed, dec_elapsed
	

test_nr = 12;
iterations = 1
plaintext = "ABCDEFghijSSdjkf"
plaintext_len = len(plaintext)


f = open("testResults/test_" + str(test_nr) + ".txt", 'w')
f_enc_raw = open("testResults/test_enc_raw_" + str(test_nr) + ".txt", 'w')
f_dec_raw = open("testResults/test_dec_raw_" + str(test_nr) + ".txt", 'w')

enc_time_sum = 0
dec_time_sum = 0


f.write('Test nr: %d\n' % test_nr)
f.write("Message: %s \n" % plaintext)
f.write("Message length: %s \n" % plaintext_len)
f.write('Iterations: %d\n' % iterations )
f.write('----------------------------')

f_enc_raw.write('Test nr: %d\n' % test_nr)
f_enc_raw.write("Message: %s \n" % plaintext)
f_enc_raw.write("Message length: %s \n" % plaintext_len)
f_enc_raw.write('Iterations: %d\n' % iterations )
f_enc_raw.write('----------------------------')

f_dec_raw.write('Test nr: %d\n' % test_nr)
f_dec_raw.write("Message: %s \n" % plaintext)
f_dec_raw.write("Message length: %s \n" % plaintext_len)
f_dec_raw.write('Iterations: %d\n' % iterations )
f_dec_raw.write('----------------------------')

for i in range(0, iterations):
	f.write("----------------Iteration %d----------------------\n" % (i+1)) 

	test_results = test(plaintext, 4)
	enc_elapsed = test_results[0]
	dec_elapsed = test_results[1]

	enc_time_sum += enc_elapsed
	dec_time_sum += dec_elapsed

	f.write("--- Encryption execution time: %s seconds ---\n" % enc_elapsed)
	f.write(("--- Decryption execution time: %s seconds ---\n" % dec_elapsed))
	f.write("-------------------------------------------\n")

	f_enc_raw.write("%s\n" % enc_elapsed)
	f_dec_raw.write("%s\n" % dec_elapsed)


enc_time_average = enc_time_sum / iterations
dec_time_average = dec_time_sum / iterations

f.write("--- Encryption average time:%s\n" % enc_time_average)
f.write("--- Decryption average time:%s\n" % dec_time_average)

f_enc_raw.write("Average:\n%s\n" % enc_time_average)
f_dec_raw.write("Average\n%s\n" % dec_time_average)
