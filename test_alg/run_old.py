import os
import timeit
import resource 


def funct():
	a = 2+2
	print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"


os.system("smem python test.py")



# timeit.timeit('funct()', number =10)

# def test():
#     """Stupid test function"""
#     L = []
#     for i in range(100):
#         L.append(i)


if __name__ == '__main__':
    
    

    print "time:", (timeit.timeit("funct()", setup="from __main__ import funct", number=100)),  "seconds"
    print "memory:" , resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "bytes"


