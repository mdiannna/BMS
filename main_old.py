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






# Old code:
'''

def encodeData(data, key):
	if key == "" or not key:
		return "no key"
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
	# final_string = ''.join(final_string)
	return final_string

def encodeDataInt(data, key):
	if key == "" or not key:
		return "no key"
	final_string = ""
	for idx, i in enumerate(key):
		# print i
		# print str(data[idx])
		final_string += data[idx]
		# print i
		i2 = int(i)
		# print i2
		for k in range(0, i2):
			extraCh = str(random.randint(0, 9))
			final_string = final_string + str(extraCh)
	# final_string = ''.join(final_string)
	return final_string


def decodeData(data, key):
	if key == "" or not key:
		return "no key"
	final_string = ""
	k = 0
	remained_to_skip = 0

	j = 0
	for char in data:
			if k == remained_to_skip:
				final_string += char
				# This is a temporary solution
				if j == len(key):
					return final_string
				remained_to_skip = int(key[j])
				j += 1
			else:
				remained_to_skip = remained_to_skip - 1
			# print "skip:"
			# print remained_to_skip
	return final_string



# Function not finished!!
def passToKey(password):
	return "32345"


# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	global key
# 	form = LoginForm(request.form, csrf_enabled=True)
# 	if request.method == "POST":
# 		# if form.validate_on_submit():
# 			key = passToKey(form.password.data)
# 			print "key=" + key
# 			message = form.username.data
# 			print encodeData(message, key)
# 			print decodeData(message, key)
# 			global logintrue
# 			logintrue = True
# 	return render_template("login.html", form=form)
'''


