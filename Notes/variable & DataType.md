
# Variable in python

- python assign same memory for same values
- Python is more memory efficient
- In python address is not variable based , but it is based on box which is data.
- we don't have constants in python



```python

num=5

#address of variable
id(num)

a=10
b=10

# id{a} and id{b} will give same address and id{10} will also give same address
id{a}
id{b}
id{10}

# constants are not threre in python

# get type of variable
type(a)

```


# DataTypes in Python

- None (it is like null when you do not assign anythin to variable)
- Numeric (float,int,complex,bool)
- List ()
- Tuple
- Set
- String
- Range
- Dictionary => All key should be unique


```python

#Complex number
num = 6 + 9j
type{num} # Comples

a = 5.6
b = int(a) # 5.6 will be converted to 5

k = float(b) # 5.0

c = complex(b.k) # 5 + 6j

bo = b<k
tyoe(bo) # bool

str = 'Vasu' # String we can use signle or double quoate


# Range

range(10) # range(0,10)

# Convert range to list
list(range(10)) # 1 to 10

list(range(2,10,2)) # difference of 2 => 2,4,6,8


```

## There are also a keyword name `global` which will create a global variable
## We can access all the global variables from a schop with `globals()` function

```python

# global variable

a = 10
b=15
c = 14
def fun():
	global a
	print(a)
	a = 12
	print(a)
	#access the global variables
	x = globals()
	# it will take all the global variables
	# if we want to change the global variable we can do following
	globals()['b'] = 200 # b will be changed
 	print(b) 

print(a)
print(b) # b will also be changed


```