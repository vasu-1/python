# Anonymous Function in Python

### Function are objects in python

### we can use anonymous function when we want to use function only at once

### these are also called lambda function

```python
from functools import reduce

f = lambda a,b : a+b # It shoule be only one expression
result = f(5,6)
print(result)

# we can get rid of this function using lambda function
def is_even(n):
	if n%2==0:
		return True
	else:
		return False

nums = [3,4,5,6,7,8,9,4]

evens = list(filter(lambda n : n%2==0,nums)) # in this we have used the lambda function

print(evens)

# same as we can use map function
#we can get rid of this function using lambda function
def update(n):
	return n*2

doubles = list(map(lambda n: n*2,evens)) # lambda function can be used here

print(doubles)



# same as we can use reduce function
sums = reduce(lambda a,b : a+b ,doubles) # labda function is used
print(sums)


```