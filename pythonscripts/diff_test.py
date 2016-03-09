def lcs(x,y):
	m = len(x)
	n = len(y)
	table = dict()

 	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				table[i,j] = 0
			elif x[i-1] == y[j-1]:
				table[i,j] = table[i-1,j-1]+1
			else:
				table[i,j] = max(table[i-1,j],table[i,j-1])

	def recon(i,j):
		if i==0 or j==0:
			return []
		elif x[i-1] == y[j-1]:
			return recon(i-1,j-1) + [x[i-1]]
 		elif table[i-1,j] >table[i,j-1]:
			return recon(i-1,j)
		else:
			return recon(i,j-1)
	return recon(m,n)























