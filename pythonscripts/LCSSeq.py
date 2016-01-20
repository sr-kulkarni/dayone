import re
import sys
import os.path

def longestSubsequence(str1,str2):
	
	#2d array of l1+1Xl2+1 initialized to 0
	l1 = len(str1)
	l2 = len(str2)
	array = [[0]*(l2+1) for i in xrange(0,l1+1)]
	for i in range(0,l1+1):
		for j in range(0,l2+1):
			if i == 0 or j == 0:
				array[i][j] = 0
			elif str1[i-1] == str2[j-1]:
				array[i][j] = array[i-1][j-1] + 1
			else:
				array[i][j] = max(array[i-1][j],array[i][j-1])

	
	index = array[l1][l2]
	lcs = [""]*(index+1)
	lcs[index] ='\0'
	i = l1
	j = l2
	while i > 0 and j > 0:
		if(str1[i-1] == str2[j-1]):
			lcs[index-1] = str1[i-1]
			i -= 1
			j -= 1
			index -= 1
		elif array[i-1][j] > array[i][j-1]:
			i -= 1
		else:
			j -= 1
	print "".join(lcs)



if __name__ == '__main__':

	if not os.path.exists(sys.argv[1]): raise Exception("Given file does not exist!")

	with open(sys.argv[1],'r') as f:
		lines = f.readlines()

	for line in lines:
		if len(line) == 0:pass
		str1,str2 = line.split(';')
		longestSubsequence(str1,str2)


	
