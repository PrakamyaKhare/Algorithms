class Stack :
	def __init__(self,size) :
		self.list = []*size
		self.size = size
		
	def push(self,item) :
		if self.list == [] :
			self.list.append(item)
			return
		self.list.insert(0,item)
		return
		
	def pop(self) :
		if self.list == [] :
			return
		self.list.pop(0)
		return
	
	def isEmpty(self) :
		return (self.list == [])

def paranMatch(exp) :
	stack = Stack(len(exp)) 
	for i in range(len(exp)) :
		if exp[i] == '(' :
				stack.push('(')
		elif exp[i] == ')' :
			if not stack.isEmpty() :
				stack.pop()
			else :
				return False
	if stack.isEmpty() :
		return True
	return False 
	
while True :
	expr = input('Enter expression ')
	print(paranMatch(expr))
