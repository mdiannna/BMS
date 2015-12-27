# Lungimea !!! daca u corespunde da eroare sau se trunchiaza!!!

import random
import string


key = "1111"
a = ""


def register(user,password):
	global key
	#  should be a function to transform pass to key2
	key = "12345"


def addData(data, key):
	final_string = ""
	for idx, i in enumerate(key):
		# print i
		# print str(data[idx])
		final_string += data[idx]
		# print i
		i2 = int(i)
		# print i2
		for k in range(0, i2):
			extraCh = random.choice(string.ascii_letters)
			final_string = final_string + str(extraCh)
	return final_string


def decodeData(data, key):
	final_string = ""
	for idx, i in enumerate(key):
		final_string += data[idx]
		i2 = int(i)
		for k in range(0, i2):
			extraCh = random.choice(string.ascii_letters)
			# final_string = final_string + str(extraCh)
	return final_string


message = input("Message:")

# print key
register("user", "Diana")
print "key=" + key

print addData(message, key)

print decodeData(message, key)


