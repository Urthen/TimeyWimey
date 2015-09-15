import shlex
import operators
import variable
import const
import errors
from statement import Statement

ops = {}
ops.update(operators.operators)

def parse(Phrases):
	Phrase = Phrases[0]
	remainder = Phrases[1:]

	# Parse strings (since we need to pay attention to quotes)
	if Phrase[0] in ['"', "'"]:
		quote = Phrase[0]
		while Phrase[-1] != quote:
			try:
				Phrase += " " + remainder.pop(0)
			except IndexError as e:
				raise errors.UnterminatedString(Phrase)

		node = const.Constant(Phrase);

	# Parse operators/commands
	elif Phrase in ops:
		operator = ops[Phrase]
		num_operands = len(operator.signature)

		operands = []

		while(len(remainder) and len(operands) < num_operands):
			operand, remainder = parse(remainder)
			operands.append(operand)

		if (len(operands) < num_operands):
			raise errors.InsufficientOperands(Phrase, num_operands, len(operands))

		node = operator(*operands)

		for operand in operands:
			operand.setParent(node)

	# Parse variable names
	elif (variable.valid_var.match(Phrase)):
		node = variable.Variable(Phrase);

	# Parse numbers
	elif (const.valid_num.match(Phrase)):
		node = const.Constant(float(Phrase))

	# Invalid token!
	else:
		raise errors.InvalidToken(Phrase)

	return node, remainder

def tokenizeLine(line):
	indentation = len(line) - len(line.lstrip())
	tokens = line.split()

	operator, remainder = parse(tokens)

	statement = Statement(operator)

	if (len(remainder) and remainder[0][0] != '#'):
		raise errors.ExpectedEOL(remainder)

	return indentation, statement

def tokenize(infile, root):
	lnum = 0
	prior_indentation = 0
	for line in infile:
		lnum += 1

		# Skip comments
		if line.strip()[0:1] == '#':
			continue

		try:
			indentation, statement = tokenizeLine(line)
		except errors.ParsingException as e:
			e.lnum = lnum
			e.line = line
			raise e

		root.addStatement(statement)