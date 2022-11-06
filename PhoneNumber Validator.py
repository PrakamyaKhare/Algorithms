"""
Phone Number Validatot Simple Algorithm 
Aurthor = Prakamya Khare
"""
def function_check(number):
	st = str(number)
	valid = '189'
	digits = 8
	check = False
	if len(st) == digits:
		first = st[0]
		for i in range(0,3):
			if  valid[i] == first:
				check = True
	return check
	
	
def check(num):
	bool = function_check(num)
	if bool:
		print("Valid")
	else:
		print("Invalid")
	
	
num = int(input("Enter number"))
check(num)