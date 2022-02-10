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