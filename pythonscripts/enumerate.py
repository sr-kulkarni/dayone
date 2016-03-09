def perms(s):
	if len(s) == 1:
		return [s]
	results = []
	for i,item in enumerate(s):
		results += [item+p for p in perms(s[:i]+s[i+1:])]

        return results


print perms('This')


