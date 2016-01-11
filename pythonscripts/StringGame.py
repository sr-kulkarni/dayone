import re

class StringGame:

	def __init__(self,string):
		if not re.match(r'[AB]+',string):raise Exception("Input string is not in the correct format! Exiting..")
		self.string = string	

	def __repr__(self):
		return self.string

	def doStuff(self,targetObj):
		flag = 1
		initial = self.string
		target = targetObj.string
		while len(initial) < len(target) and flag ==1:
			flag = 0
			if initial+'A' in target:
				initial = initial+'A'
				flag = 1
			changed = initial[::-1] 
 			if changed+'B' in target: 
				initial = changed + 'B'
				flag =1
	
		return (initial == target)





if __name__ == '__main__':

	str1 = raw_input("Enter the initial string : ")
	str2 = raw_input("Enter the target string : ")
        initial = StringGame(str1)
        target = StringGame(str2)        

	result = initial.doStuff(target)
        
        print "Your strings are : "
	print initial
	print target

	if(result): print "These strings satisfy our criteria"
	else: print "These strings do not satisfy our criteria!"







