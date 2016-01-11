
def doStuff(initial,target):
	flag = 1
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





initial = raw_input("Enter the initial string : ")
target = raw_input("Enter the target string : ")

result = doStuff(initial,target)

print initial
print target

if(result): print "Yo this is correct"
else: print "This is not corect."







