import re

class Entry:
	
	
	def __init__(self,data):
		if not (data >= 0 and data <= 255): raise Exception("{} is not in correct range!".format(data))
		self.data = data

class Octet:

	EntryList = []

	def __init__(self,string):
		entries = re.findall(r'\d+',string) #In case user is giving the input, sanitize it beforehand
		flag = 1
		for entry in entries:
			
			if (flag == 1 and int(entry) == 0): 
				raise Exception("{} cannot be the first entry in an octet".format(entry))
                

			try:
				d_entry = Entry(int(entry))
			except:
				print "This Input is invalid : {}".format(d_entry)
			self.EntryList.append(entry)
			flag = 0


	def __repr__(self):
		return '.'.join(self.EntryList)

#Lets do a quick check on what we did. 
#A different class for Entry doesn't make sense actually. Just doing it for some hands on. 

octet = Octet("127.0.0.1")
print "First octet is : "
print octet

octet2 = Octet("0.0.1.1")
print "Second octet is :"
print octet2
		



	
