from app import app
from forms import testForm
from flask import render_template, request, redirect
import random

import os
import timeit
import resource 
from statistics import median, mean
# from app.forms import

NR_OF_TESTS = 10

@app.route('/', methods=['GET', 'POST'])
def index():
	form = testForm(request.form, csrf_enabled=True)

	algorithm = 'BMS'
	msg_len = 10
	key_len = 10
	enc_time = []
	dec_time = []


	nr_of_tests = 0
	enc_time_median = []
	enc_time_avg = []

	if request.method == 'POST':
		nr_of_tests = int(form.nr_tests.data)
		print "nr of tests:", nr_of_tests
		
		# algorithm[0] = "BMS1"
		msg_len *= random.randint(1, 10)
		key_len += 1

		enc_time_sum = 0
		
		
		for i in range(nr_of_tests):
			print "hello"
			temp_enc_time =(timeit.timeit("funct()", setup="from app.views import funct", number=1)) 
			enc_time_sum += temp_enc_time
			temp_enc_time *= 1000
			# print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"
			enc_time.append(temp_enc_time)  
			print "time:",temp_enc_time,  "seconds"
			# !!!!!!!!!!!!!!!!!!!!!!
			dec_time.append(50 + temp_enc_time*100000+20)  

			# algorithm.append('Algorithm')
		for i in range(nr_of_tests):
			enc_time_median.append(median(enc_time))
			enc_time_avg.append(mean(enc_time))
		print "median", enc_time_median
		
		# return render_template("chart2.html", form=form, algorithm=algorithm, msg_len=msg_len, 
		# 	key_len=key_len, enc_time=enc_time, dec_time=dec_time, nr_of_tests=nr_of_tests)



	
	return render_template("index.html", form=form, algorithm=algorithm, msg_len=msg_len, 
			key_len=key_len, enc_time=enc_time, dec_time=dec_time, nr_of_tests=nr_of_tests, 
			enc_time_median=enc_time_median, enc_time_avg=enc_time_avg)


def funct():
	a = 2+2
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"
	
