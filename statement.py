from enum import enum

class State(Enum):

class Statement(object):
	def __init__(self, operator):
		self.operator = operator
		self.vars = self.operator.vars
		operator.parent = self
		self.state = 'unexecuted'

	def __str__(self):
		return "#%d: %s" % (self.position, str(self.operator))

	def execute(self):
		print("Result:", self.operator.evaluate())

	def propagateChange(self, var, val):
		self.parent.propagateChange(self.position, var, val)