from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, PasswordField, SubmitField


class testForm(Form):
	algorithm = TextField('Algorithm:')
	nr_tests = IntegerField('Nr. of tests:')
	msg_len = IntegerField('Message length:')
	key_len = IntegerField('Key length:')
	submit = SubmitField('ok')