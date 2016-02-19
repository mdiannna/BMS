from app import app, db
from app import login_manager
from flask import render_template, request, redirect
from forms import LoginForm, RegisterForm, AddDataForm
from app.models import UserData, PersonalData
from flask.ext.login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


from encryption.encryption import simpleEncrypt, blockEncrypt, randomBlockEncrypt, randomBlockEncryptV4
from encryption.decryption import simpleDecrypt2, randomBlockDecrypt, randomBlockDecryptV4
from encryption.keylib import readKey, printK, firstKeyToKey, keyTextSeparation



import random
import string
import copy

# !!!!!!!!!!!! temporary key for each user!!!!!!!!!

# temporary using as global variables
block_pos = 0
del_pos = 2
block_size = 0
key_len = 0

key = [0] * 10000

@login_manager.user_loader
def load_user(userid):
	user = UserData.query.get(userid)
	return user


# logintrue = False
# key = "32345"

def encrypt(plaintext, key, key_len, block_size):
	return randomBlockEncryptV4(plaintext, key, key_len, block_size)

def decrypt(ciphertext, key, key_len, block_size):
	res = 0
	try:
		res = randomBlockDecryptV4(ciphertext, key, key_len, block_size)	
	except:
		pass
	return res



@app.route('/')
def index():
	return render_template("firstpage.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form, csrf_enabled=True)
	FK = [0] * 10000
	global key
	global block_size
	global key_len

	error = False
	
	
	if request.method == 'POST':
		
		first_key = str(form.key.data)
		first_key_len = len(first_key)
		readKey(int(first_key),  FK, first_key_len)

		resultsK = firstKeyToKey(FK, first_key_len, block_pos, del_pos)
		key  = resultsK[0]
		block_size = resultsK[1]
		# print "*************block block_size = ", block_size
		key_len = first_key_len - FK[del_pos]-1 - FK[block_pos] - 1

		if key_len < 0 or not key:
			error = True

		else:
			plaintext = form.username.data 
			username = encrypt(plaintext, key, key_len, block_size)
			# password = generate_password_hash(form.password.data)
			# print "hash:", password
			plaintext = form.password.data
			print "passw:", plaintext
			password = encrypt(plaintext, key, key_len, block_size)

			plaintext = form.firstname.data
			firstname = encrypt(plaintext, key, key_len, block_size)

			plaintext = form.lastname.data
			lastname = encrypt(plaintext, key, key_len, block_size)
			

			plaintext = str(form.tel.data)
			tel = encrypt(plaintext, key, key_len, block_size)

			user = UserData(username=username,
				password=password,
				firstname=firstname,
				lastname=lastname,
				tel=tel)
			db.session.add(user)
			db.session.commit()
			# key = ""
			return redirect('/')
	
	return render_template("register.html", form=form, error = error)


@app.route('/adddata', methods=['GET', 'POST'])
@login_required
def adddata():
	global key
	global block_size
	global key_len

	FK = [0] * 10000

	form = AddDataForm(request.form, csrf_enabled=True)
	print "-----------key=", key
	
	if request.method == "POST":

		first_key = str(form.key.data)
		first_key_len = len(first_key)
		readKey(int(first_key),  FK, first_key_len)

		resultsK = firstKeyToKey(FK, first_key_len, block_pos, del_pos)
		key  = resultsK[0]
		block_size = resultsK[1]
		# print "*************block block_size = ", block_size
		key_len = first_key_len - FK[del_pos]-1 - FK[block_pos] - 1
		print "-----------key=", key
	
		plaintext = form.secret.data
		secret = encrypt(plaintext, key, key_len, block_size)
		plaintext = form.nr_passport.data
		nr_passport = encrypt(plaintext, key, key_len, block_size)
		plaintext = form.color.data
		color = encrypt(plaintext, key, key_len, block_size)

		# username = "nick"
		# password = "password"
		# password = generate_password_hash(password)
		user_id = current_user.get_id()
		data = PersonalData(secret=secret, 
			nr_passport=nr_passport,
			color=color,
			user_id=user_id)
		db.session.add(data)
		db.session.commit()
		return redirect('/viewuserdata')

	return render_template("adddata.html", form=form)



def decodeItem(item, key):
	ciphertext = item.firstname
	item.firstname = decrypt(ciphertext, key, key_len, block_size)
	ciphertext = item.lastname
	item.lastname = decrypt(ciphertext, key, key_len, block_size)
	ciphertext = item.tel
	item.tel = decrypt(ciphertext, key, key_len, block_size)
	ciphertext = item.username
	item.username = decrypt(ciphertext, key, key_len, block_size)
	# item.secret = decodeData(item.secret, key)

def decodePersonalData(item, key):
	ciphertext = item.secret
	item.secret = decrypt(ciphertext, key, key_len, block_size)
	ciphertext = item.nr_passport
	item.nr_passport = decrypt(ciphertext, key, key_len, block_size)
	ciphertext = item.color
	item.color = decrypt(ciphertext, key, key_len, block_size)

@app.route('/viewalldata', methods=['GET', 'POST'])
@login_required
def viewalldata():
	global key

	# key = request.args['key']
	print "key=", key
	encodedata = UserData.query.all()
	decodedata = copy.deepcopy(encodedata)
	for item in decodedata:	
		print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
		decodeItem(item, key)
	return render_template("viewalldata.html", encodedata=encodedata, decodedata=decodedata)


@app.route('/viewuserdata', methods=['GET', 'POST'])
@login_required
def viewuserdata():
	global key
	print "key=", key

	user_id = current_user.get_id()

	# key = request.args['key']
	print "key=", key
	encodedata = UserData.query.get(user_id)
	print "--------------user_id=", user_id
	print "encodedata=", encodedata
	item = copy.deepcopy(encodedata)
	decodeItem(item, key)


	encodedPersonalData = PersonalData.query.filter_by(user_id=user_id).all()
	decodedPersonalData  = copy.deepcopy(encodedPersonalData )
	for item in decodedPersonalData:
		decodePersonalData(item , key)
	# personalData = PersonalData.query.get()

	
	return render_template("viewuserdata.html", encodedata=encodedata, item=item, 
			encodedPersonalData=encodedPersonalData, decodedPersonalData=decodedPersonalData )



@app.route('/login', methods = ['POST', 'GET'])
def login():
	global key
	global block_size
	global key_len
	
	FK = [0] * 10000
	form = LoginForm(request.form, csrf_enabled=True)
	error = ''
	print "signin"
	# if form.validate_on_submit():
	if request.method == "POST":
		print '************'
		# print form.username.data, form.password.data
		# password = form.password.data
		# password = encodeData(raw_password, key)
		# password = generate_password_hash(form.password.data)
		first_key = form.username.data
		print "first_key:", first_key

		first_key = str(form.key.data)
		first_key_len = len(first_key)
		readKey(int(first_key),  FK, first_key_len)

		resultsK = firstKeyToKey(FK, first_key_len, block_pos, del_pos)
		key  = resultsK[0]
		block_size = resultsK[1]
		# print "*************block block_size = ", block_size
		key_len = first_key_len - FK[del_pos]-1 - FK[block_pos] - 1


		username = form.username.data
		print "username:", username
		password = form.password.data
		print "password:", password
		
		users = UserData.query.all()
		print "########"
		for user in users:
			ciphertext = user.username
			try:
				user_username = decrypt(ciphertext, key, key_len, block_size)
				ciphertext = user.password
				user_password = decrypt(ciphertext, key, key_len, block_size)
				print "user_name:", user_username
				print "user_pass:", user_password
			except:
				user_username = None
				user_password = None
			if username == user_username and password == user_password:
				# if check_password_hash(user_password, password):
					login_user(user)
					print 'logged in successfully'
					return redirect('/viewuserdata')
					break
		error = "login unsuccesful"
		print error
	return render_template("login.html", form = form, error=error)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


# @app.route('/deletedata')
# def deletedata():
# 	data = UserData.query.all()
# 	if request.method == 'POST':
# 		db.