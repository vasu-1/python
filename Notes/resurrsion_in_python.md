# Recursion in Python

```python

import sys

sys.setrecursionlimit(123) # we can set recursion limit
print(sys.getrecursionlimit) # we can print recursion limit 
# by default the recursion limit is 1000


def greet():
	# print('Hello')
	# greet()
	pass

greet()

```

# Factorial Program in Python using Recursion

```python
def fact(n):
	if(n==0):
		return 1

	return n * fact(n-1)

print(fact(5))
```
