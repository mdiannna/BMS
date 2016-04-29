from app import app
from forms import testForm
from flask import render_template, request, redirect
import random

import os
import timeit
import resource 
# from app.forms import

NR_OF_TESTS = 10

@app.route('/', methods=['GET', 'POST'])
def index():
	update = 'False'
	form = testForm(request.form, csrf_enabled=True)

	algorithm = 'BMS'
	msg_len = 10
	key_len = 10
	enc_time = []
	dec_time = []


	nr_of_tests = 0

	if request.method == 'POST':
		nr_of_tests = int(form.nr_tests.data)
		print "nr of tests:", nr_of_tests
		update = 'True'
		print "posted"
		# algorithm[0] = "BMS1"
		msg_len *= random.randint(1, 10)
		key_len += 1
		
		for i in range(nr_of_tests):
			temp_enc_time =(timeit.timeit("funct()", setup="from app.views import funct", number=1)) 
			print "time:", (timeit.timeit("funct()", setup="from app.views import funct", number=1)) ,  "seconds"
			# print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"
			enc_time.append(temp_enc_time)  
			# !!!!!!!!!!!!!!!!!!!!!!
			dec_time.append(temp_enc_time)  

			# algorithm.append('Algorithm')



	
	return render_template("index.html", form=form, update=update, algorithm=algorithm, msg_len=msg_len, 
			key_len=key_len, enc_time=enc_time, dec_time=dec_time, nr_of_tests=nr_of_tests)


def funct():
	a = 2+2
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"
	
