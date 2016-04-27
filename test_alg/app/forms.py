from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, PasswordField, SubmitField


class testForm(Form):
	nr_tests = IntegerField('Nr. of tests:')
	submit = SubmitField('ok')