

class NotDefinedYet(Exception):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "Not defined yet: $%s" % self.name

########################################################################################################################
class ParsingException(Exception):
	pass

class InsufficientOperands(ParsingException):
	def __init__(self, operator, required, provided):
		self.operator = operator
		self.required = required
		self.provided = provided

	def __str__(self):
		return "Insufficient operands; operator '%s' required %d, %d provided." % (self.operator, self.required, self.provided)

class InvalidToken(ParsingException):

	def __init__(self, token):
		self.token = token;

	def __str__(self):
		return "Invalid Token: " + self.token

class UnterminatedString(ParsingException):
	def __init__(self, token):
		self.token = token;

	def __str__(self):
		return "Unterminated String: " + self.token

class ExpectedEOL(ParsingException):

	def __init__(self, remainder):
		self.remainder = remainder;

	def __str__(self):
		return "Expected end of line, but saw: '%s'" % " ".join(self.remainder)

class IncorrectIndentation(ParsingException):

	def __init__(self, indentation, expected):
		self.indentation = indentation;
		self.expected = expected;

	def __str__(self):
		return "Inconsistent indentation, prior line was %s, current line is %s" % (expected, indentation)