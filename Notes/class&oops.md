# OOPS In Python

## Class :-


```python

class Computer:
	"""docstring for Computer"""
	# def __init__(self, arg):
	# 	super(Computer, self).__init__()
	# 	self.arg = arg
		

	def config(self):
		print("i5 i6 i7")


a = 5
comp1 = Computer()
# without any parameter
comp1.config()
#access function inside the class
Computer.config(comp1)
```

## Class variabe or parameter

```python

class Computer:
	"""docstring for Computer"""

	def __init__(self, cpu,name):
		super(Computer, self).__init__()
		self.cpu = cpu
		self.name = name
		

	def config(self):
		print(self.cpu, self.name)


comp1 = Computer('i7','hp')
comp1.config()

```

