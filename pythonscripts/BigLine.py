import heapq
import argparse
import sys
import os.path

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('Path')
	args = parser.parse_args()
	string = str(args)
        #a,'\'',c,'\'',d = string
	a,b,c = string.split('\'')
	print "Your file is : "+b
	
	if not os.path.exists(b): raise Exception("The file specified does not exist!")

	with open(b,"r") as f:
		n = f.readline()
	try:
		n += 1
		if n <= 0: raise Exception("Number of lines needs to be greater than 0")
	except TypeError:
	    	print "The number needs to be an integer"

	lines = open(b).readlines()
	heap = heapq.nlargest(int(n),lines,len)
	print "".join(heap)


