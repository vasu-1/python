
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


#dsd