# Functions in Python


```python
# we  can use normal function and we canreturn a value as well

# we can also return two value in python

def add_sub(a,b):
	x = a+b
	y = a-b
	return x,y

res = add_sub(6,5)
print(res)  #output : (11, 1)
# we can also fetch a perticulat value like print(res[1])
# we can return multiple values in python

def add_sub_mul(a,b):
	x = a+b
	y = a-b
	z = a*b
	g = a/b
	return x,y,z,g

res = add_sub(6,5)
print(res) # output (11, 1, 30, 1.2)
# and we can fetch like an array

#we can also do this
res1,res2 = add(5,6)  

```

### in python there is no pass by value or pass by reference
### in python we do pass by id


## Python funcion pass parameters Technique

```python

def add(*b):
	c = 0
	for i in b:
		c += i

	return c

c = add(1,2,3,4) 
# when we are not sure with the function arguements then we can use this variable length parameter

# there are also concept of the function default parameters
# same as cpp and java
# there is also default arguement function
# like fun(a,b=3) # if there is no arguement for b then it will automatically take b=3
```