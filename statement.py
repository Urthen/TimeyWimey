from enum import Enum

class State(Enum):
	Unexecuted = 1
	Executing = 2
	Waiting = 3
	Exhausted = 4


class Statement(object):
	def __init__(self, operator):
		self.operator = operator
		self.vars = self.operator.vars
		operator.parent = self
		self.state = State.Unexecuted

	def __str__(self):
		return "#%d: %s" % (self.position, str(self.operator))

	def execute(self):
		print("Result:", self.operator.evaluate())

	def propagateChange(self, var, val):
		self.parent.propagateChange(self.position, var, val)