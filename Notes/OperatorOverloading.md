# Operator Overloading In Python


```python


class Student(object):
	def __init__(self, arg1, arg2):
		super(Student, self).__init__()
		self.arg1 = arg1
		self.arg2 = arg2


	def __add__(self,other):
		m1 = self.arg1 + other.arg1
		m2 = self.arg2 + other.arg2
		s3 = Student(m1,m2)

		return s3


	def __gt__(self,other):
		r1 = self.arg1 + self.arg1
		r2 = other.arg2 + other.arg2

		if r1 > r2:
			return True
		else:
			return False


	def __str__(self): # it will override the method and it will show the values of the calss object
		return '{} {}'.format(self.arg1,self.arg2) 



s1 = Student(2,3)
s2 = Student(4,5)

s3 = s1 + s2
print(s3.arg2)


if s1 > s2:
	print("S1 is high")
else:
	print("s2 is high")


a=10
print(a.__str__()) # by default in integer it will show the value

print(s1.__str__()) # by defalt it will show the address of the object
# but we can override in the class as method
# and it is showing the value of the object


```