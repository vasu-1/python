# Abstract Class in Python

- Abstraction is not supported in oython bydefault
- We need to import the module named `abc`
- Bydefaule we can create an object of abstract class
- but after that module we cannot create an object of an abstract class

- Abstract class  atleast one abstract method
- `Abstract methods does't have defenition but it only has declaration`


```python
from abc import ABC, abstractmethod

class Com(ABC):

	@abstractmethod
	def process(self):
		pass

class Desktop(Com):
	pass


class Laptop(Com):
	def process():
		print("Working")



# coma = Com()
# coma.process()
#we can't make object of abstract class

comb = Laptop()
# we can do it as because it has atleast one method

# comb = Desktop()
# We ca't do it as it is an abstract
```
