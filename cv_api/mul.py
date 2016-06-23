from sys import version_info
import numpy as np
print "enter the nuber of columns for first matrix"
#m = input('enter the value for m:')
#n = input('enter the value for n:')
a=np.matrix([[1,2,3],[3,4,5],[5,2,1]])
b=np.matrix([[1,1,3],[6,4,5],[5,2,99]])
#matrix = m*n
i=0
j=0
#a=10,10
for i in range(len(a)):
	for j in range(len(a)):
		print np.matrix[i][j]


	#	print np.matrix[i][j]
