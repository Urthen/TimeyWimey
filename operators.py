import token
from node import Node

class SetOperator(Node):
	signature = 'aa'

	def __init__(self, a, b):
		super().__init__()
		self.a = a;
		self.b = b;

	def __str__(self):
		return "= %s %s" % (str(self.a), str(self.b))

	def evaluate(self):
		val = self.b.evaluate()
		self.parent.propagateChange(self.a, val)
		return val

class PrintOperator(Node):
	signature = 's'

	def __init__(self, a):
		super().__init__()
		self.a = a

	def __str__(self):
		return 'print %s' % str(self.a)

	def evaluate(self):
		print(self.a.evaluate())
		return True

operators = {
	'=':		SetOperator,
	'print':	PrintOperator
}