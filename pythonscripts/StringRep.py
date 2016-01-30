import sys
import os
import re

def doStuff(orig,list2):
        checker = []
	def replaceOkay(orig,el0,el1):

                def allGood(checker,pos,l1):
			for i in range(0,l1):
				if pos+i in checker: return False
			for i in range(0,l1):
				checker.append(pos+i)
			return True

		#First find the occurences of substring
                occurs = [m.start() for m in re.finditer(el0, orig)]      
                #Now see if any of those elements were changed earlier
	        for pos in occurs:
			if allGood(checker,pos,len(el1)):
				return pos
		return 0

	for el in list2:
		if el[0] in orig:
			#print "replacing  "+el[0]+" with "+el[1] 
			pos = replaceOkay(orig,el[0],el[1])
			if pos != 0: 
				print "replacing  "+el[0]+" with "+el[1]
              			print "Position is : "+str(pos)
				temp = orig[(pos+len(el[0])):]
				print "Temp is  "+temp
			        print orig[0:pos]
				orig = orig[0:pos]+el[1]
				print "Left part now is : "+orig
				orig += temp
				print orig
	return orig


if __name__ == '__main__':
	filename = sys.argv[1]
	if not os.path.exists(filename): raise Exception("Your file ain't nowhere bro")
        with open(filename,'r') as f:
		lines = f.readlines()
        for line in lines:
		orig, rest = line.split(';')
		rest = rest.strip('\n')
                if len(rest)%2 == 1:raise Exception("Not even!")
	        listin = rest.split(',')
                list2 =  zip(listin[0::2],listin[1::2])
		answer = doStuff(orig,list2)
		print answer



