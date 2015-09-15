class Node(object):
	def __init__(self):
		self.vars = []

	def setParent(self, parent):
		self.parent = parent;
		self.parent.vars.extend(self.vars)

	def propagateChange(self, var, val):
		self.parent.propagateChange(var, val)