from analyzation1 import *
from test import *
from simple_parser import *
from test_parser import *

print('--- RULES --->')
print('type lex for LEXER')
print('type pars for PARSER')

command = input()
#command = 'pars'
if command == 'lex':
	tests = test()
elif command == 'pars':
	pars = test_parser()

