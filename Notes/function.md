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

# if we are not sure in which manner there is an arguement
# at this time we can use this technique to work with this
def data(name,age):
	print("name ", name)
	print("age ", age)

data('vasu',34) # normal passing parameter
data(23,'Vasu') # it will not give axpected output
data(age=45,name='vasu') # it will give expected output because we are specifying the name of the arguement



# Variable length parameter
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

## Keyworded Variable Length Arguments in Python

```python

def data(name,**attr):
	print(name)
	print(attr)

	for i,j in attr.items(): #fetch the key and value pair
		print(i, j)


data('vasu',age=20,clas=8,num=23)

```



## Passing list in function

```python

def count(lst):
	even=0
	odd=0
	for i in lst:
		if i%2 == 0:
			even+=1
		else:
			odd+=1
	return even,odd


lst=[1,2,3,4,5,6,7,8,6,5,2]
even,odd=count(lst)
print(even,odd)
#format in string input
print("even : {} and odd : {}".format(even,odd))

```