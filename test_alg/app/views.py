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
test_args = ""

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

		msg_len *= random.randint(1, 10)
		key_len += 1


		enc_dec = "enc"
		data_statistics = calcPerformance(enc_dec, key_len, msg_len, algorithm, nr_of_tests)
		enc_time = data_statistics[0]
		enc_time_median = data_statistics[1]
		enc_time_avg = data_statistics[2]
		enc_time_mode = data_statistics[3]

		enc_dec = "dec"
		data_statistics = calcPerformance(enc_dec, key_len, msg_len, algorithm, nr_of_tests)
		dec_time = data_statistics[0]
		dec_time_median = data_statistics[1]
		dec_time_avg = data_statistics[2]
		dec_time_mode = data_statistics[3]
	
	return render_template("index.html", form=form, algorithm=algorithm, msg_len=msg_len, 
			key_len=key_len, enc_time=enc_time, dec_time=dec_time, nr_of_tests=nr_of_tests, 
			enc_time_median=enc_time_median, enc_time_avg=enc_time_avg, enc_time_mode=enc_time_mode,
			dec_time_median=dec_time_median, dec_time_avg=dec_time_avg, dec_time_mode=dec_time_mode,
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
	return max_k


def test_enc_BMS(args):
	command = "python " + "BMS_inloc" + ".py" + args
	os.system(command)
	print command
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"

def test_dec_BMS(args):
	command = "python " + "BMS_inloc" + ".py" + args
	os.system(command)
	print command
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"

def test_enc_AES(args):
	command = "python " + "AES_inloc" + ".py" + args
	os.system(command)
	print command
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"

def test_dec_AES(args):
	command = "python " + "AES_inloc" + ".py" + args
	os.system(command)
	print command
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"


def calcPerformance(enc_dec, key_len, msg_len, algorithm, nr_of_tests):

	msg = "test"
	key = 1234

	global test_args 
	test_args = " " + str(msg) + " " + str(key)			
	function_name = "test_" + enc_dec + "_" + algorithm

	time = []
	
	time_median = []
	time_avg = []
	time_mode = []

	for i in range(nr_of_tests):
		temp_time =(timeit.timeit(function_name + "(test_args)", setup="from app.views import " + function_name + "," + "test_args", number=1)) 
		temp_time *= 1000
		# print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"
		time.append(temp_time)  
		# !!!!!!!!!!!!!!!!!!!!!!
	

		# algorithm.append('Algorithm')
	for i in range(nr_of_tests):
		time_median.append(median(time))
		time_avg.append(mean(time))
		
	time_int = map(int, time)
	print "MODE:", calcMode(time_int)
	mode = mean(calcMode(time_int))

	for i in range(nr_of_tests):
		time_mode.append(mode);

	return time, time_median, time_avg, time_mode



	
