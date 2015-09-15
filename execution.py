from statement import Statement
from errors import NotDefinedYet

class Execution(Statement):

	def __init__(self, parent):
		self.parent = parent
		self.statements = []

	def addStatement(self, statement):
		statement.position = len(self.statements)
		statement.parent = self
		self.statements.append(statement)

	def run(self):
		for statement in self.statements:
			print(statement)

			try:
				statement.execute()
			except NotDefinedYet as e:
				print(e)

	def propagateChange(self, position, var, val):
		print("Changed %s to %s from line %d" % (var, str(val), position))