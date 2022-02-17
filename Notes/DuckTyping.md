# Duck Typing In Python

- It is a method to do polymorphision


```python


class Pycharm:

	def execute(self):
		print("Compiling Running from Pycharm")


class MyEditor:

	def execute(self):
		print("Compiling Running From MyEditor")


class Laptop(object):
	# def __init__(self, arg):
	# 	super(Laptop, self).__init__()
	# 	self.arg = arg


	def execute(self):
		print("Spell Check")
		print("Compiling Running")


	def code(self,ide):
		ide.execute() # it does.t chck for object type


ide = MyEditor() # if you put PyCharm then it will also be ok
# but in that case it will call pycharm class method execute

lap1 = Laptop()

lap1.code(ide)


```