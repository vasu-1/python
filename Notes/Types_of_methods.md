# Types of methods !!



```python
class Student:

	#class variables
	school = "telusko"

	def __init__(self,m1,m2,m3):
		#instance variable
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
		

	# instance methods

	def avg(self):
		return (self.m1 + self.m2 + self.m3)/3


	def get_m1(self):
		return self.m1


	def set_m1(self,value):
		self.m1 = value


	#class methoods

	@classmethod
	def info(self):
		return self.school	


	# static method
	@staticmethod
	def stat():
		print("This is for operation and if we want to do stuff for other classes then we can use this !")


s1 = Student(34,35,36)
s2 = Student(45,46,47)
print(s1.avg())
print(Student.info())

Student.stat()

```