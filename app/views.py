from app import app, db
from app import login_manager
from flask import render_template, request, redirect
from forms import LoginForm, RegisterForm, AddDataForm
from app.models import UserData
from flask.ext.login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

import random
import string
import copy
# !!!!!!!!!!!! temporary key for each user!!!!!!!!!

@login_manager.user_loader
def load_user(userid):
	user = UserData.query.get(userid)
	return user


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
				remained_to_skip = int(key[j])
				j += 1
			else:
				remained_to_skip = remained_to_skip - 1
			print "skip:"
			print remained_to_skip
	return final_string



# Function not finished!!
def passToKey(password):
	return "32345"

# logintrue = False
key = "32345"

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

@app.route('/')
def index():
	return render_template("firstpage.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form, csrf_enabled=True)
	return render_template("register.html", form=form)


@app.route('/adddata', methods=['GET', 'POST'])
@login_required
def adddata():
	form = AddDataForm(request.form, csrf_enabled=True)
	if request.method == "POST":
		global key
		firstname=encodeData(form.firstname.data, key)
		lastname=encodeData(form.lastname.data, key)
		tel=encodeDataInt(form.tel.data, key)
		secret=encodeData(form.secret.data, key)

		username = "nick"

		password = "password"
		password = generate_password_hash(password)

		data = UserData(username=username,
			password=password,
			firstname=firstname,
			lastname=lastname,
			tel=tel, 
			secret=secret)
		db.session.add(data)
		db.session.commit()
		return redirect('/viewdata')

	return render_template("adddata.html", form=form)



def decodeItem(item, key):
	item.firstname = decodeData(str(item.firstname), key)
	item.lastname = decodeData(item.lastname, key)
	item.tel = decodeData(item.tel, key)
	item.secret = decodeData(item.secret, key)


@app.route('/viewdata', methods=['GET', 'POST'])
@login_required
def viewdata():
	encodedata = UserData.query.all()
	decodedata = copy.deepcopy(encodedata)
	for item in decodedata:
		global key
		print key
		decodeItem(item, key)
	return render_template("viewdata.html", encodedata=encodedata, decodedata=decodedata)



@app.route('/login', methods = ['POST', 'GET'])
def login():
	global key
	form = LoginForm(request.form, csrf_enabled=True)
	error = ''
	print "signin"
	# if form.validate_on_submit():
	if request.method == "POST":
		print '************'
		print form.username.data, form.password.data
		# password = form.password.data
		# password = encodeData(raw_password, key)
		# password = generate_password_hash(form.password.data)
		password = form.password.data
		print password
		users = UserData.query.filter_by(username=form.username.data).all()
		print "########"
		for user in users:
			print "username:", user.username
			print "pass:", user.password
			if check_password_hash(user.password, password):
				login_user(user)
				print 'logged in successfully'
				return redirect('/viewdata')
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