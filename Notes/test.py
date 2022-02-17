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