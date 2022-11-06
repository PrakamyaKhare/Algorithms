def startsWith(str1,str2):
	size = len(str2)
	count = 0
	for i in range(size):
		if str2[i] == str1[i]:
			count += 1
	if count == size:
		return True
	return False
	
str1 = 'Hello  World'
str2 = 'He'
ans = startsWith(str1,str2)
print(ans)
print(str1.startswith(str2))
