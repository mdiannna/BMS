from app import app
from forms import testForm
from flask import render_template, request, redirect
import random

import os
import timeit
import resource 
from statistics import median, mean
from collections import Counter
from itertools import groupby
# from app.forms import

NR_OF_TESTS = 10

@app.route('/', methods=['GET', 'POST'])
def index():
	form = testForm(request.form, csrf_enabled=True)

	show_chart = False
	exception = False

	algorithm = 'BMS'
	msg_len = 10
	key_len = 10
	enc_time = []
	dec_time = []


	nr_of_tests = 0
	enc_time_median = []
	enc_time_avg = []
	enc_time_mode = []

	if request.method == 'POST':
		exception = False
		show_chart = True

		try:
			nr_of_tests = int(form.nr_tests.data)
		except:
			exception = True
			print "EXCEPTION:", exception
			nr_of_tests = 0
			show_chart = False

		print "nr of tests:", nr_of_tests
		
		# algorithm[0] = "BMS1"
		msg_len *= random.randint(1, 10)
		key_len += 1

		enc_time_sum = 0
		
		
		for i in range(nr_of_tests):
			# print "hello"
			temp_enc_time =(timeit.timeit("funct()", setup="from app.views import funct", number=1)) 
			enc_time_sum += temp_enc_time
			temp_enc_time *= 1000
			# print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"
			enc_time.append(temp_enc_time)  
			# # print "time:",temp_enc_time,  "seconds"
			# !!!!!!!!!!!!!!!!!!!!!!
			dec_time.append("Not computed")  

			# algorithm.append('Algorithm')
		for i in range(nr_of_tests):
			enc_time_median.append(median(enc_time))
			enc_time_avg.append(mean(enc_time))
			# enc_time_mode.append(mode(enc_time))
			# enc_time_mode = Counter(enc_time).most_common()

		# data = Counter(enc_time)
		# data.most_common()   # Returns all unique items and their counts
		# temp = data.most_common(1)
		# mode_sum = 0

		# for j in range(len(temp)):
		# 	temp2 = temp[j]
		# 	# print "tem[2:", temp2
		# 	temp3 = temp2[j]
		# 	mode_sum += temp3;
		# 	# print "tem[3:", temp3
		# enc_mode = mode_sum/len(temp)

		enc_time_int = map(int, enc_time)
		print "MODE:", calcMode(enc_time_int)
		enc_mode = mean(calcMode(enc_time_int))

		for i in range(nr_of_tests):
			enc_time_mode.append(enc_mode);

		
		# return render_template("chart2.html", form=form, algorithm=algorithm, msg_len=msg_len, 
		# 	key_len=key_len, enc_time=enc_time, dec_time=dec_time, nr_of_tests=nr_of_tests)



	
	return render_template("index.html", form=form, algorithm=algorithm, msg_len=msg_len, 
			key_len=key_len, enc_time=enc_time, dec_time=dec_time, nr_of_tests=nr_of_tests, 
			enc_time_median=enc_time_median, enc_time_avg=enc_time_avg, enc_time_mode=enc_time_mode,
			exception=exception, show_chart=show_chart)

def calcMode(list):	
	d = {}
	for elm in list:
		try:
			d[elm] += 1
		except(KeyError):
			d[elm] = 1
	
	keys = d.keys()
	max = d[keys[0]]
	
	for key in keys[1:]:
		if d[key] > max:
			max = d[key]

	max_k = []		
	for key in keys:
		if d[key] == max:
			max_k.append(key),

	# print "max:", max

	# print("MODESSSS")
	# for key in max_k:
	# 	if d[key] == max:
	# 		print key
	# return max_k, max
	return max_k



def funct():
	# a = 2+2
	os.system("python test.py 10 asd")
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"
	
