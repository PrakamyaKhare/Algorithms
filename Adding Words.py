def adding_words(*args):
	length = len(args)
	st = ''
	for i in range(length):
		if i == (length-1):
			word = args[i]
			st += word
		else:
			word = args[i]
			st += word + '-'
	return st
	
print(adding_words('this','is','awesome'))