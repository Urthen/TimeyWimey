from tokenize import tokenize
from execution import Execution
import errors
import sys

infile = open('test.tw')

print("Reading File...")

root = Execution(None)

try:
	lines = tokenize(infile, root)
except errors.ParsingException as e:
	print("Error parsing line %d:\n>>> %s\n%s" % (e.lnum, e.line.strip(), str(e)))
	sys.exit(1)

print("Executing Timestream...")
root.run()
