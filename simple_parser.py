from analyzation1 import *
from expr_node import *


class simple_parser:
	def __init__(self, test_path):
		self.test_prog = test_path
		self.analyz = analyzation(self.test_prog)
		

		
		#self.parseFactor()

	def main(self):
		return self.parseExp()


	def parseFactor(self):
		#print('parseFactor')
		self.analyz.lex_next()
		token = self.analyz.lex_get()
		#print( token.get_type(), " ",  token.get_value())
		if token.get_type() == 'id':
			self.analyz.lex_next()
			return IdNode(token)
		elif token.get_type() == 'int':
			self.analyz.lex_next()
			return IntegerNode(token)
		elif token.get_value() == '(':
			#print("скобка!")
			expr = self.parseExp()
			op = self.analyz.lex_get()
			if op.get_value() != ')':
				str_err =token.get_pos()+ " Missing ')'" 
				raise ValueError(str_err);
			self.analyz.lex_next()
			return expr
		else:
			#print('WRONG OPERAND')
			str_err = token.get_pos()+ " Wrong operand"
			raise ValueError(str_err);
	
	def parseTerm(self):
		#print('parseTerm1')
		left = self.parseFactor()
		op = self.analyz.lex_get()
		while op.get_value() == "*" or op.get_value() == "/":
			right = self.parseFactor()
			left = BinOpNode(left, right, op)
			op = self.analyz.lex_get()

		return left

	def parseExp(self):
		left = self.parseTerm()
		op = self.analyz.lex_get()
		while op.get_value() == "+" or op.get_value() == "-":
			right = self.parseTerm()
			left = BinOpNode(left, right, op)
			op = self.analyz.lex_get()

			
		return left

