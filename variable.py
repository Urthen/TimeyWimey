from errors import NotDefinedYet
from node import Node
import re

valid_var = re.compile('^[a-zA-Z][a-zA-Z0-9]*$')

class Variable(Node):
	def __init__(self, name):
		super().__init__()
		self.vars = [self]
		self.name = name
		self.value = None

	def __str__(self):
		if self.value:
			return "$%s (%s)" % (self.name, str(self.value))
		else:
			return "$" + self.name

	def evaluate(self):
		if self.value:
			return self.value
		else:
			raise NotDefinedYet(self.name)