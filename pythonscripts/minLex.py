import sys

class MinStic:
	
	def __init__(self,string,string2):
		if not isinstance(string,str) or not isinstance(string2,str): raise Exception("Input is not in the correct format!")
		self.firstString = string
		self.nextString = string2

	def __repr__(self):
		return str("'"+ self.firstString + "' , '" + self.nextString + "' ")

	def doStuff(self):
		l1 = len(self.firstString)
		l2 = len(self.nextString)
		s1 = self.firstString
		s2 = self.nextString
		ans = []
		i = 0
		j = 0

		def compare(str1,str2,i,j):
			#print "comapring"
			k = min(len(str1)-i,len(str2)-j)
			for it in range(0,k):
				if str1[i+it] < str2[j+it]:
					#print str1[i+it] +" is lesser than " + str2[j+it]
					return -1
				else:
					#print "greater second"
					return 1
			return (len(str2)-j) - (len(str1)-i)



		while i < l1 or j < l2:
			#print " in the loop now"
			if(i == l1):
				ans.append(s2[j:])
				break
			elif(j == l2):
				ans.append(s1[i:])
				break
			elif compare(s1,s2,i,j) < 0:
				ans.append(s1[i])
				i += 1
			else:
				ans.append(s2[j])
				j += 1
				

		



		return ''.join(ans)




if __name__ == '__main__':
	wordCount = input()
	if wordCount < 1 or wordCount > 5: raise Exception()
	array = []

	for i in range(wordCount):
		str1 = sys.stdin.readline().rstrip('\n')
		str2 = sys.stdin.readline().rstrip('\n')
		M = MinStic(str1,str2)
		array.append(M.doStuff())

	for stuff in array:
		print stuff
