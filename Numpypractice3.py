import numpy as np

#matrix with zeros and ones

mat_1=np.ones((5,4))
print(mat_1)
print(" ")

mat_0=np.zeros((3,4))
print(mat_0)
print(" ")

#array with only one value
array=np.full((4,5), 9)
print(array)
print(" ")

#ravel-to flatten the array i.e to convert it to 1d array
my_array=np.array([1,2,3,4,5,6,7,8,9])
my_array.ravel()
print("")

#transpose- switch rows and columns in a matrix
reshaped=my_array.reshape(3,3)
print(reshaped)
reshaped.transpose()
print(" ")

#vsplit-split an array into multiple sub-arrays vertically
random_array=np.random.randint(0,5, size=(4,5))
split=np.vsplit(random_array,2)
print(" ")

#hsplit-split arrays horizontally
rand_arr=np.random.randint(1,5,9)
split=np.hsplit(rand_arr,3)
print(" ")

#concatente
a=np.array([2,2,3,4,5,7])
b=np.array([3,5,6,7])
c=np.concatenate((a,b))
print(c)
print(" ")

#vstack-to stack arrays vertically
x=np.random.randint(6,size=(2,2,2))
print(x)
y=np.random.randint(6,size=(2,2,2))
z=np.random.randint(6,size=(2,2,2))
vstack_=np.vstack((x,y,z))
print(vstack_)
print(" ")

#hstack
ist=np.array([1,2,3,4]).reshape(-1,1)
second=np.array([5,6,7,8]).reshape(-1,1)
third=np.array([9,10,11,12]).reshape(-1,1)
hstack_=np.hstack((ist,second,third))
print(" ")

#linear algebra with numpy arrays using "linalg"
#det-returns determinant of matix
A=np.random.randint(6,size=(3,3))
det_=np.linalg.det(A)
print(det_)
print(" ")

#inv-inverse of a matrix
inv_=np.linalg.inv(A)
print(inv_)
print(" ")

#Eig-computes the eigenvalues and right eigenvectors for a square matrix
eig_=np.linalg.eig(A)
print(eig_)
print(" ")

#matmul- perfoms multiplication of matrix
P=([[2,3],[4,5]])
Q=([[5,6],[6,7]])
matmul_=np.matmul(P,Q)