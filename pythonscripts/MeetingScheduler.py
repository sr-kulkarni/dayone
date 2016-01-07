class Schedule(object):
	slots = [0]*48
	def __init__(self,start=0,end=0):
		for i in range(int(start/0.5),int(end/0.5)):
			self.slots[i] = 1;
		
	def __repr__(self):
		print "Today's Schedule : Busy times -"
		for i in range(0,48):
                        #print self.slots[i]
			if(self.slots[i] == 1): print "{} to {}".format((i*0.5),float((i+1)*0.5))
                return " END "
	def add(self,start,end): 
		for i in range(int(start/0.5),int(end/0.5)):
			self.slots[i] = 1

	def findSlots(self,s2):
		for i in range(0,48):
			if(self.slots[i] == 0 and s2.slots[i] == 0): print "Common Slot : {} - {}".format((i*0.5),float((i+1)*0.5))

		
if __name__ == '__main__':
	
	sc1 = Schedule(0,1.5)
        sc1.add(11.5,13)
	#print sc1
	
	sc2 = Schedule(0,4.5)
        sc2.add(6.5,22.5);

        #print "SC2 is "
        #print sc2

        print "Common Time Slots Available : "
	sc1.findSlots(sc2)

        
