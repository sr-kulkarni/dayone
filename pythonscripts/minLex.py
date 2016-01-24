class MinStic:
	
	def __init__(self,string,string2):
		if not isinstance(string,str) or not isinstance(string2,str): raise Exception("Input is not in the correct format!")
		self.firstString = string
		self.nextString = string2

	def __repr__(self):
		return str("'"+ self.firstString + "' , '" + self.nextString + "' ")

	def doStuff(self):
		print self


if __name__ == '__main__':
	wordCount = input()

	for i in range(wordCount):
		str1 = raw_input()
		str2 = raw_input()
		M = MinStic(str1,str2)
		M.doStuff()
	