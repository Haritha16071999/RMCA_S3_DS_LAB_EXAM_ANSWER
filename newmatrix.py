import numpy as np
A= np.array([[5,8,10],[4,9,1],[7,3,2]])
B= np.array([[15,18,11],[14,19,16],[17,13,12]])
print("multiplication of matrix A")
s=(np.multiply(A,A))
print(s)
print("transpose AA")
W=s.T
print(W)
print("multiplication of matrix B")
q=(np.multiply(B,B))
print(q)
print("multiplication of 2BB")
R=(2*q)
print(R)
print("transpose of 2BB")
Z=(R.T)
print(Z)
print("subtraction of (AA)T -(2BB)T :")
print(np.subtract(W,Z))



