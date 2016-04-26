import os
import timeit
import resource 
import sys
from termcolor import colored


def funct():
	a = 2+2
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"


def run(algorithm):
	os.system("python " + algorithm + "_inloc.py")
	# print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss , "bytes"

def run_BMS():
	return 0


if __name__ == '__main__':
	
	try:
		command = sys.argv[1] 
		if not command == 'BMS' and not command == 'AES':
			exception
	except:
		print colored("Error! Please specify algorithm, as following:", "red")
		print '"python run.py BMS"', "or", '"python run.py AES"'
		exit()


	print  colored("Running" + command, "green")
	for i in range(10):
		print "time:", (timeit.timeit("run(command)", setup="from __main__ import run, command", number=1)),  "seconds"
		print('------------')
	    # print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"


