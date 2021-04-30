from Lexer import Lexer
from Buffer import Buffer
from State import State
from dict_of_states import dict_of_states

class analyzation:
	def __init__(self, Path):
		self.Separators = [' ', '\n', '\t', '\0', '\r']	
		self.Key_words = ['string','integer','shortint','smallint','byte','int64','word','longword','cardinal','uint64','BigInteger',
		'real','double', 'single', 'decimal','boolean', 'char','False','True','and', 'array', 'begin', 'case', 'const', 'do', 'downto',
		'else', 'end','file', 'for', 'foreach', 'function', 'goto', 'if', 'in', 'label', 'mod', 'nil','not', 'of', 'or', 'packed', 
		'procedure', 'program', 'record', 'repeat', 'set', 'then','to', 'type', 'until', 'var', 'while', 'with', 'writeln']
		self.curr_symbs = ['','']
		self.input_file = open(Path, 'r')
		self.error_state = False
		#ТЕКУЩИЕ СИМВОЛ И ПОЗИЦИЯ
		self.curr_p = -1
		self.curr_s = ""
		
		
#	
#		START
#
	def analyzer(self):
		while True:
			lexem = self.get_lex()
			return lexem
			if  lexem.get_type() == 'eof':
				break
#
#		MAIN
#
	def get_lex(self):
		buff = Buffer()
		stat = State()
		dict_state = dict_of_states()

		if  self.error_state:
			self.error_state  = False
			return Lexer(self.curr_p - len(buff.get_buff()), 'eof', '', '')

		if self.curr_symbs[1] == '':
			self.curr_symbs[1] = self.get_next_symb()

		while True:
			self.get__next()

			if stat.get_state() == 1:
				next_state = dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[0]))
				stat.set_state( next_state  )
			
			#print( self.curr_p,'  ', self.curr_symbs[0], self.define_symb(self.curr_symbs[0]) )
			next_state = dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[1]))
			self.state_action(stat.get_state(),buff)
			#print('  ', stat.get_state(), '->' ,next_state)
			
			if stat.get_state() == 7:
				self.error_state = True
				lex_len = len(buff.get_buff())-1
				if self.curr_symbs[0] == "":
					lex_len = len(buff.get_buff())
				return Lexer(self.curr_p - lex_len, 'error', buff.get_buff(), buff.get_buff())

			stat.set_state( next_state )
			
			if  stat.get_state() == 1:
				if buff.get_buff() != "":
					return self.create_lex(buff, dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[0])))

			if stat.get_state() == 3:
				if buff.get_buff() == "":
					return Lexer(self.curr_p - len(buff.get_buff()), 'eof', '', '')
				else:
					return self.create_lex(buff, dict_state.find_state( 1, self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[0])))
#
#		MAIN
#

	def get_next_symb(self):
		next_s = self.input_file.read(1)
		if next_s :
			return next_s
		else:
			return ""



	def get__next(self):
		self.curr_p += 1
		self.curr_symbs[0] = self.curr_symbs[1]
		self.curr_symbs[1] = self.get_next_symb()


	def state_action(self, stat, buff):
		if stat == 4 or stat == 5 or stat == 6 or stat == 9 or stat == 41 or stat == 3 or stat == 7:
			buff.add_buff(self.curr_symbs[0])


	def define_symb(self,symb):
		if symb == "":
			return symb
		elif symb.isalpha():
			if symb == "e":
				return "E"
			else:
				return "L"
		elif symb.isdigit():
			return "N"
		elif symb in self.Separators:
			return "S"
		elif symb == "+" or symb == "*":
			return "I"
		elif symb == ">" or symb == "<":
			return "W"
		elif symb == "'" or symb == '"':
			return "V"
		else:
			return symb


	def create_lex(self, buff, state):
		value = buff.get_buff()
		if state == 4:
			if buff.get_buff().find('.') != -1:
				type_s = 'float'
				value = float(buff.get_buff())
			else:
				type_s = 'number'	
			'''lex_str = buff.get_buff()
			i = buff.get_buff().find('..')
			if i != (-1):
				with open("result.txt", "a") as f:
					f.write(str(self.curr_p - len(buff.get_buff())+1) + "	" + type_s + "	" + lex_str[0:i] +'\n')
					f.write(str(self.curr_p - len(buff.get_buff())+1+i) + "	" + 'delimiter' + "	" + lex_str[i:i+2] +'\n')
				buff.clear_buff()
				buff.add_buff(lex_str[i+2:])'''
		elif state == 5:
			type_s = 'string'
		elif state == 6:
			if buff.get_buff() in self.Key_words:
				type_s = 'reserved id'
			else:
				type_s = 'id'
		elif state == 9:
			type_s = 'delimiter'
		elif state == 8:
			type_s = 'comment'
		elif state == 7:
			type_s = 'error'
		else:
			type_s = state

		new_lex = Lexer(self.curr_p - len(buff.get_buff())+1, type_s, buff.get_buff(), value)
		buff.clear_buff()
		return new_lex
	