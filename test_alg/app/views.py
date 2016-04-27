from app import app
from forms import testForm
from flask import render_template, request, redirect
import random
# from app.forms import


@app.route('/', methods=['GET', 'POST'])
def index():
	update = 'False'
	if update == 'False':
		algorithm =['BMS', 'AES']
	msg_len = 10
	key_len = 10
	enc_time = 0.3
	dec_time = 0.1

	if request.method == 'POST':
		update = 'True'
		print "posted"
		# algorithm[0] = "BMS1"
		msg_len *= random.randint(1, 10)
		key_len += 1
		enc_time += 0.001
		dec_time += 0.0001
		# algorithm.append('Algorithm')



	form = testForm(request.form, csrf_enabled=True)
	return render_template("index.html", form=form, update=update, algorithm=algorithm, msg_len=msg_len, 
			key_len=key_len, enc_time=enc_time, dec_time=dec_time)