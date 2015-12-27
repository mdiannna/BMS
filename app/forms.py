# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField,  SubmitField, PasswordField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import  UserData


class LoginForm(Form):
	username = TextField('Username:')
	password = PasswordField('Password:')
	submit = SubmitField('OK')


class RegisterForm(Form):
	username = TextField('Username:')
	password = PasswordField('Password:')
	submit = SubmitField('OK')

class AddDataForm(Form):
	firstname = TextField('Name:')
	lastname = TextField('Last name:')
	tel = TextField('Telephone:')
	secret = TextField('What is your secret?')
	submit = SubmitField('OK')


