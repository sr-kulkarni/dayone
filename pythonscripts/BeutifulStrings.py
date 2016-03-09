from collections import Counter
import re

if __name__ == '__main__':
	
	string = "yo yo honey singhe!"
	string = re.sub(r'[^a-z]+','',string.lower())
	print string
        #s = re.sub(r'[^a-z]', '', s.lower())
	c = Counter(string)
	print c
