from errors import NotDefinedYet
from node import Node
import re

valid_num = re.compile('^[0-9]+(.[0-9]+)?$')

class Constant(Node):

	def __init__(self, value):
		super().__init__()
		self.value = value

	def __str__(self):
		return str(self.value)

	def evaluate(self):
		return self.value;