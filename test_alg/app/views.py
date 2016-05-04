from app import app
from forms import testForm
from flask import render_template, request, redirect
import random

import os
import commands
import timeit
import resource 
from statistics import median, mean
from collections import Counter
from itertools import groupby
import string
import random
import math



NR_OF_TESTS = 10
test_args = ""

@app.route('/', methods=['GET', 'POST'])
def index():
	form = testForm(request.form, csrf_enabled=True)

	show_chart = False
	exception = False

	algorithm = 'BMS'
	nr_of_tests = 0
	msg_len = 0
	key_len = 0

	enc_time = []
	enc_time_median = []
	enc_time_avg = []
	enc_time_mode = []
	dec_time = []
	dec_time_median = []
	dec_time_avg = []
	dec_time_mode = []

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

		algorithm = form.algorithm.data
		
		if not (algorithm == 'BMS' or algorithm == 'AES'):
			exception = True
		else:
			msg_len = form.msg_len.data
			key_len = form.key_len.data


			enc_dec = "enc"
			data_statistics_enc = calcPerformance(enc_dec, key_len, msg_len, algorithm, nr_of_tests)

			enc_time = data_statistics_enc[0]
			enc_time_median = data_statistics_enc[1]
			enc_time_avg = data_statistics_enc[2]
			enc_time_mode = data_statistics_enc[3]

			enc_dec = "dec"
			data_statistics = calcPerformance(enc_dec, key_len, msg_len, algorithm, nr_of_tests)

			dec_time = data_statistics[0]
			dec_time_median = data_statistics[1]
			dec_time_avg = data_statistics[2]
			dec_time_mode = data_statistics[3]

			print "enc_time:", enc_time, "dec time:", dec_time
		
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
	# command = "python " + "BMS_inloc" + ".py" + args
	command = './BMS_cpp/encrypt' + args
	print command
	return commands.getstatusoutput(command)[1].replace('\n', '')
	# print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"

def test_dec_BMS(args):
	# command = "python " + "BMS_inloc" + ".py" + args
	command = './BMS_cpp/decrypt' + args
	print command
	return commands.getstatusoutput(command)[1].replace('\n', '')
	# print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"

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


def generateMsg(msg_len):
	msg = ""
	for i in range(msg_len):
		msg += random.choice(string.letters)
	return msg

def generateKey(key_len):
	key = 0
	for i in range(key_len):
		key = key*10 + random.randint(1, 9)
	return key

def calcPerformance(enc_dec, key_len, msg_len, algorithm, nr_of_tests):

	msg = generateMsg(msg_len)
	key = generateKey(key_len)

	global test_args 
	test_args = " " + str(msg) + " " + str(key)			
	function_name = "test_" + enc_dec + "_" + algorithm

	time = []
	
	time_median = []
	time_avg = []
	time_mode = []

	for i in range(nr_of_tests):
		# temp_time =(timeit.timeit(function_name + "(test_args)", setup="from app.views import " + function_name + "," + "test_args", number=1)) 

		temp_time = float(eval(function_name + "('" + test_args + "')"))
		# eval(test_dec_BMS())
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



	
@app.route('/brute_force_chart', methods=['GET', 'POST'])
def brute_force_chart():
	key_len = []
	block_size = []

	nr_of_tests = 100

	for b in range(1, nr_of_tests):
		k = (256.0 * math.log10(2)) / (math.log10(9.0 * b))
		key_len.append(int(round(k)))
		block_size.append(b)

	print "Key length:", key_len
	print "Block size:", block_size
	return render_template("brute_force_chart.html", key_len=key_len, block_size=block_size, nr_of_tests=nr_of_tests)


@app.route('/compile')
def compile():
	os.system("g++ BMS_cpp/main_encrypt.cpp BMS_cpp/encryption.cpp BMS_cpp/decryption.cpp BMS_cpp/keylib.cpp" )
	os.system('g++ -o BMS_cpp/encrypt BMS_cpp/main_encrypt.cpp BMS_cpp/encryption.cpp BMS_cpp/decryption.cpp BMS_cpp/keylib.cpp')
	os.system("g++ BMS_cpp/main_decrypt.cpp BMS_cpp/encryption.cpp BMS_cpp/decryption.cpp BMS_cpp/keylib.cpp" )
	os.system('g++ -o BMS_cpp/decrypt BMS_cpp/main_decrypt.cpp BMS_cpp/encryption.cpp BMS_cpp/decryption.cpp BMS_cpp/keylib.cpp')
	# os.system('xxd -c10 -b ./BMS_cpp/main')
	# os.system('./BMS_cpp/main')
	comp_output = "<strong>C++ compilation output:<strong><br>"+ commands.getstatusoutput('./BMS_cpp/encrypt')[1].replace('\n', '<br>')
	comp_output += "<br>---<br>"+ commands.getstatusoutput('./BMS_cpp/decrypt')[1].replace('\n', '<br>')

	print "****", comp_output.replace('<strong>', "").replace('<br>', '\n')

	return comp_output
