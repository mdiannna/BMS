from Crypto.Hash import MD5
import timeit



h = MD5.new()


def encrypt(message):
	# print "Encryption:"
	
	h.update(message)
	ciphertext = h.hexdigest()

	return ciphertext 
	


def decrypt(ciphertext):
	# print "Decryption:"
	return ""


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
	


test_nr = 1;
iterations = 50
plaintext = "ABCDEFghijSSdjkf"
plaintext_len = len(plaintext)


f = open("testResults/hash_test_" + str(test_nr) + ".txt", 'w')
f_enc_raw = open("testResults/hash_test_enc_raw_" + str(test_nr) + ".txt", 'w')
f_dec_raw = open("testResults/hash_test_dec_raw_" + str(test_nr) + ".txt", 'w')

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
