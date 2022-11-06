"""
2. String Compression for example aabbccc = a2b2c3
"""

def stringCompression(string) :
	freq = {}
	for char in string :
		if not char in freq :
			freq[char] = 0
	for i in string :
		if i in freq :
			freq[i] += 1
	print(freq)
	
st = 'aabbccc'
print(stringCompression(st))