# Method Overloading And Overriding

## Method Overloading

- It is not supported in python
- We are not doing it directly
- but we are doing it indirectly by assigning values to `None` and doing `else-if` stuff.

```python

class Student(object):
	def __init__(self, arg1, arg2):
		super(Student, self).__init__()
		self.arg1 = arg1
		self.arg2 = arg2


	def sum(self,a=None,b=None,c=None): # by default it is None
		if(a!=None and b!= None and c!= None):
			s = a+b+c

		elif(a!= None and b!= None):
			s = a+b;
		else:
			s=a
		return s




s1 = Student(2,3)
print(s1.sum(1,2))
print(s1.sum(1,2,5))
print(s1.sum(4))




```


## Method Overriding

```python

class A:

	def show(self):
		print("A Show")


class B(A):


	def show(self):
		print("B Show")


a1 = A()
a1.show()

b1 = A()
b1.show() # it will only show the method of A


 

```