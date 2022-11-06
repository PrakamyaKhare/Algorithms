class Graph :
	def __init__(self,size) :
		self.adj = [[0]*size for i in range(size)]
		self.size = size
	
	def check(self,src,des) :
		if src > self.size or des > self.size or src < 0 or des < 0 :
			return False
		return True
		
	def addEdge(self,src,des) :
		if self.check(src,des) :
			self.adj[src][des] = 1
			self.adj[des][src] = 1
			return
		print('Invalid Input')
		
	def removeEdge(self,src,des) :
		if self.check(src,des) :
			self.adj[src][des] = 0
			self.adj[des][src] = 0
			return
		print('Invalid Input')
		
	def printList(self) :
		for row in self.adj :
			for col in row :
				print(col,' ')
			print()
		return
		
g  = Graph(4)
g.addEdge(1,2)
g.addEdge(2,3)
g.printList()