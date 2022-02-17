# Inheritence In Python


```python

class A(object):
	def __init__(self, arg):
		super(A, self).__init__()
		self.arg = arg
		print("init A")


	def feature1(self):
		print("feature 1 A")

	def feature4(self):
		print("feature 4 A")

	
		

class B(A):
	def __init__(self, arg1,arg):
		super().__init__(arg)
		self.arg1 = arg1
		print("init B")



	def feature3(self):
		print("feature 3 B")
		self.feature1()

	def feature4(self):
		print("feature 4 B")
		super().feature4()


a1 =B(1,2)	
a1.feature3()
a1.feature4()
```