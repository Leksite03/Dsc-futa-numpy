import numpy as np

#getting an array of random numbers
#using rand() i.e uniformly distributed from 0 to 1
my_rand=np.random.rand(5)
print(my_rand)
print(" ")
#2d array
my_2d_rand=np.random.rand(4,6)
print(my_2d_rand)
print(" ")

#using randn()
my_randn=np.random.randn(8)
print(my_randn)
print(" ")
#2d array
my_2d_randn=np.random.randn(5,7)
print(my_2d_randn)
print(" ")

#using randint()
my_randint=np.random.randint(20, size=10)
print(my_randint)
print(" ")
#2d array
my_2d_randint=np.random.randint(5,15, size=(9,10))
print(my_2d_randint)
print(" ")

#converting 1-dim array to 2-dim array
arr=np.random.rand(36)
arr.reshape(6,6)
print(arr)
print(" ")

#locating the max and min value in an array
#max
arr_1=np.random.randint(0,20,10)
print(arr_1)
print(" ")
arr_1_max=arr_1.max()
print(arr_1_max)
print(" ")
#min
arr_1_min=arr_1.min()
print(arr_1_min)
print(" ")


#using argmax() and argmin() functions to locate the index of the max or min val in an arr
arg_max=arr_1.argmax()
print(arg_max)
print(" ")
arg_min=arr_1.argmin()
print(arg_min)
print(" ")

#indexing/selecting elements or group of elements from a numpy array
choose_num=arr_1[6] #gives the element at index 6
print(choose_num)
print(" ")

#to get the range of val using ":"
get_arr=arr_1[2:7] #gives the list of elements from index 2 to 7(exclusive)
print(get_arr)
print(" ")
get_arr_2=arr_1[4:] #gives the list of elements from index 4 to the end of the array
print(get_arr_2)
print(" ")

#selecting elements in a 2d array using [][] or [,]
_2d_array=np.array([[1,2,3], [4,5,6], [7,8,9]])
select=_2d_array[0][2]
print(select)
print(" ")
#using [,]
select_=_2d_array[2,2]
print(select_)
print(" ")

#selecting 2-d array using ":"
sel=_2d_array[:2,1:]
print(sel)
print(" ")

sel_=_2d_array[0]   #select the first row of the array 
print(sel_) 
print(" ")

s_=_2d_array[:2] #select every val before row 2
print(s_)
print(" ")

#performing conditional and logical selections on array using &(AND), |(OR), <, > and == operators
new_arr=np.arange(2,12)
new_arr_=new_arr>6 #returns true where the elements are greater than 6
print(new_arr_)
print(" ")

new_array=new_arr_[new_arr_] #returns only the elements greater than 6
print(new_array)
print(" ")

#using the combination of conditional and logical &(and) operators

_new_array=new_arr[(new_arr>4) & (new_arr<10)]
print(_new_array)
print(" ")

#using | (or) operator

_new_arr=new_arr[(new_arr>3) | (new_arr<9)]
print(_new_arr)
print(" ")

#broadcasting
my_array_2=np.array([1,2,3,4,5,6,7,8,9])
my_array_2[0:4]=33
print(my_array_2)
print(" ")

#performing arithmetic operations
arr=new_arr
mul=arr*arr # multiplication
print(mul)
print(" ")
sub=arr-arr #subtraction
print(sub)
print(" ")
add=arr+arr #addition
print(add)
print(" ")
div=arr/arr #division
print(div)
print(" ")
#performing universal functions
sqrt_=np.sqrt(arr) #square root of each element
print(sqrt_)
print(" ")
exp_=np.exp(arr) #exponentials
print(exp_)
print(" ")
sin_=np.sin(arr) #sine 
print(sin_)
print(" ")
cos_=np.cos(arr) #cosine
print(cos_)
print(" ")
tan_=np.tan(arr) #tangent
print(tan_)
print(" ")
log_=np.log(arr) #logarithm
print(log_)
print(" ")
sum_=np.sum(arr) #sum
print(sum_)
print(" ")
std_=np.std(arr) #standard derivation
print(std_)
print(" ")
