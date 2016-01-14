import sys

def findDups(total,array):
	obssum = 0
	expected = total*(total+1)/2
	for element in array:
		obssum += int(element)	
	print abs(expected-obssum)
	
	




if __name__ == '__main__':
	with open(sys.argv[1],"r") as f:
		lines = f.readlines()

        for line in lines:
		if len(line) == 0: pass
		line2,notimp = line.split('\n')
		number,rest = line2.split(';')
		array = rest.split(',')
		number = int(number)
		number -= 2
		findDups(number,array)	


