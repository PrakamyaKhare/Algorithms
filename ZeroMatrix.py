"""
1.Zero matrix an algorithm to set all rows and columns to zero if an element of the matrix is 0

Prakamya Khare
"""
import numpy as np

def setZero(M,ro,co) :
	rows = len(M)
	cols  = len(M[0])
	res = [[0]*cols]*rows
	for i in range(rows) :
		for j in range(cols) :
			res[i][j] += M[i][j]
	for c in range(cols) :
			res[ro][c] = 0
	for r in range(rows) :
		res[r][co] = 0
	print(res)
	return res
	
def zeroMatrix(M) :
	rows = len(M)
	cols = len(M[0])
	res = None
	for i in range(rows) :
		for j in range(cols) :
			if M[i][j] == 0 :
				for r in range(rows) :
					for c in range(cols) :
						M[i][c] = 0
					M[r][c] = 0
	print(np.matrix(M))
	
M = [[1,2,0],[0,3,4]]
N = [[1,2,3],[4,5,0],[5,4,1]]
zeroMatrix(M)	
zeroMatrix(N)