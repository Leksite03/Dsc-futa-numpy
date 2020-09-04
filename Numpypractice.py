import numpy as np

#numpy array
my_array=np.array([1,2,3,4,5,6,7,8,9])
print(my_array)
print(" ")
#2d array
_2d_array=np.array([[1,2,3], [4,5,6], [7,8,9]])
print(_2d_array)
print(" ")

#using the arange() function
arr=np.arange(0,13,2)
print(arr)
print(" ")

#getting the shape of an array
shaped=my_array.shape
print(shaped)
("  ")

#using the reshape() function
reshaped=my_array.reshape(3,3)
print(reshaped)
("  ")

#zeros()
list_2=np.zeros((5,6))
print(list_2)
print(" ")

#eye() function/identity
list_3=np.eye(6)
print(list_3)
print(" ")

#multiplication of matrix
list_4=np.arange(1,19,2).reshape(3,3)
print(list_4)
print(" ")
list_5=np.arange(1,10).reshape(3,3)
print(list_5)
print(" ")
mul=np.dot(list_4,list_5)
print(mul)
print(" ")

#addition of element in matrix
#add all the elements of matrix
sum_mat=np.sum(mul)
print(sum_mat)
print(" ")
#sum along rows
sum_row=np.sum(mul,axis=1)
print(sum_row)
print(" ")
#sum along cols
sum_col=np.sum(mul,axis=0)
print(sum_col)
print(" ")


