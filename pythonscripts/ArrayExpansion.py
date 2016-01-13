class EArray:

	def __init__(self,count = 50,user_input = None):
		self.count = count
		self.array = [0]*count
		print self.array
		for i in range(0,len(user_input)):
			print user_input[i]
			self.array[i] = user_input[i]

		self.array = user_input


	def __getitem__(self,element):
		return self.array[element]

	def __repr__(self):
		for i in range(0,self.count):print self.array[i] 
		return " "

 	def replace(self):
		ColonCount = 0
		for i in range(0,self.count):
			if(self.array[i] == ':'):ColonCount += 1
		

 		print ColonCount





