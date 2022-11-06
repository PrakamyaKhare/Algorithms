class Vector(object) :
	"""
	Vector class for little vector operations for example addition ,subtraction,addition
	
	"""
	def __init__(self,v) :
		self.v = v
		self.error_statement = 'error both vector must be of same size'
		
	def __add__(self,v2) :
		if type(v2) == type(1) :
			vec = []
			for e in self.v :
				vec.append(e - v2)
			return Vector(vec)
		
		if len(self.v) != len(v2.v) :
			return self.error_statement
		
		vec = []
		for e1,e2 in zip(self.v,v2.v) :
			vec.append(e1+e2)
			
		return Vector(vec)
		
	def __mul__(self,v2) :
		if type(v2) ==type(1) :
			vec = []
			for e in self.v :
				vec.append(e * v2)
			return Vector(vec)
			
		if len(self.v) != len(v2.v) :
			return self.error_statement
			
		vec = []
		for e1,e2 in zip(self.v,v2.v) :
			vec.append(e1*e2)
		
		return Vector(vec)
		
	def __pow__(self,n) :
		new_v = []
		for e in self.v :
			   new_v.append(e**n)
		return Vector(self.v)
		
	def __sub__(self,v1) :
		if type(v1) == type(1) :
			vec = []
			for e in self.v :
				vec.append(e - v1)
			return Vector(vec)
		
		if len(self.v) != len(v1.v) :
			return self.error_statement
		
		vec = []
		for e1,e2 in zip(self.v,v1.v) :
			expr = e1 - e2
			vec.append(expr)
			
		return Vector(vec)
		
	def __truediv__(self,v1) :
		if type(v1) == type(1) :
			vec = []
			for e in self.v :
				vec.append(e/v1)
			return Vector(vec)
		
		if len(self.v) != len(v1.v) :
			return self.error_statement
		
		vec  = []
		for e1,e2 in zip(self.v,v1.v) :
			vec.append(e1 / e2)
		return Vector(vec)
	
	def __repr__(self,) :
		print(self.v)
		return ''
	
a = Vector([1,2,3,6,7])
b = Vector([1,2,3,6,7])
g = a/b
c = a + b
d = a - b
e = a * b
ee = a * 2
f = a ** 3
gg = a/2
print(c)
print(d)
print(e)
print(f)
print(ee)
print(g)
print(gg)