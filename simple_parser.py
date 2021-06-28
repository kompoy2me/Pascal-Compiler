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
				#err_token = Lexer(op.get_pos(), 'error', op.get_orig(), op.get_value() )
				#return Node(None, None, err_token)
			self.analyz.lex_next()
			return expr
		else:
			#print('WRONG OPERAND')
			str_err = token.get_pos()+ " Wrong operand"
			raise ValueError(str_err);
			#err_token = Lexer(token.get_pos(), 'error', token.get_orig(), token.get_value() )

			#return Node(None, None, err_token)
	
	def parseTerm(self):
		#print('parseTerm1')
		left = self.parseFactor()
		#print('parseTerm2')
		#if left.getValue().get_type() == 'error':
		#	return left
		op = self.analyz.lex_get()
		#if op.get_type() == 'error':
		#	return BinOpNode(left, None, op)
		#print('parseTerm, op = ', op.get_value())
		while op.get_value() == "*" or op.get_value() == "/":
			right = self.parseFactor()
			#if right.getValue().get_type() == 'error':
			#	return right
			left = BinOpNode(left, right, op)
			#if left.getValue().get_type() == 'error':
			#	return left
			op = self.analyz.lex_get()
			#if op.get_type() == 'error':
			#	return BinOpNode(left, None, op)

		return left

	def parseExp(self):
		#print('parseExp')
		left = self.parseTerm()
		#print(left.getValue().get_value())
		#if left.getValue().get_type() == 'error':
		#	return left
		op = self.analyz.lex_get()
		#if op.get_type() == 'error':
		#	return BinOpNode(left, None, op)
		#print('parseExp, op = ', op)
		while op.get_value() == "+" or op.get_value() == "-":
			#print('цикл, op = ', op.get_value())
			right = self.parseTerm()
			#if right.getValue().get_type() == 'error':
			#	return right
			left = BinOpNode(left, right, op)
			#if left.getValue().get_type() == 'error':
			#	return left
			op = self.analyz.lex_get()
			#if op.get_type() == 'error':
			#	return BinOpNode(left, None, op)
			
		return left

