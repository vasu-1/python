# Inner Class

```python

class Student:

	def __init__(self,name,roll,brand,cpu,ram):
		#instance variable
		self.name = name
		self.roll = roll
		self.lap = self.Laptop(brand,cpu,ram)
		

	# instance methods

	def show(self):
		print(self.name, self.roll)
		self.lap.show()

	
	class Laptop(object):
		def __init__(self, brand, cpu, ram):
			super(Student).__init__()
			self.brand = brand
			self.cpu = cpu
			self.ram = ram

		def show(self):
			print(self.brand,self.cpu,self.ram)
			




# s1 = Student("vasu",21)
# print(s1.name,s1.roll)
# s1.show()

s2 = Student("vasu",23,"hp","i7",4)
s2.show()
```