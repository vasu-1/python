# Python in Python

## Ways of Creating Arrays in Numpy ::

```python

from numpy import *

#array
arr = array([1,2,3,5,6]) #it is optional to specifyy 'i' next to [] in numpy
# in array module you have to specify the type before [] like 
# arr= array('i',[1,2,3]) something like this

print(arr[1])
print(arr.dtype) #print the type of the array

#linkspace (in numpy)
arr = linspace(0,15,16) # start stop step
# if we don't specify step then it will convert default by its stop means range
print(arr[2])

#arange (in nummpy)
arr2 = arange(1,15,2) # different will be 2
print(arr2)

#logspace (in numpy)
arr3 = logspace(1, 40, 5) # different will be in log of 5
print(arr3)

#zeros (in numpy)
arr4 = zeros(5) # creat an array of 5 element with zerso
arr5 = ones(6) # create an array of 6 element with ones
print(arr4)
print(arr5)

```

## Two Dimensional Array !

```python

from numpy import *


arr1 = array([
		[1,2,3],
		[4,5,6]
	])

print(arr1.dtype) # data type
print(arr1.ndim) # number of dimension1

print(arr1.shape) # number of row and column

print(arr1.size) # entire size

arr2 = arr1.flatten() # multi dim  to single
print(arr2)

arr3 = arr2.reshape(3,2) # single to multi
print(arr3)

arr4 = arr2.reshape(1,3,2) # 3D array from single array
print(arr4)


m = matrix('1 2 3 4 ; 2 3 4 5')

m1 = matrix('1 2 ; 3 4 ; 6 7') # create amatrix 
m2 = matrix('3 4 5 ; 2 3 4')
print(m)
print(m1)
print(diagonal(m)) # print diagonal element
print(m.min())  # minimum element and we can also do max
m3 = m1 * m2 # multiply matrices
print(m3)



````