import re
from Lexer import Lexer
from Buffer import Buffer
from State import State
from dict_of_states import dict_of_states

class analyzation:
	def __init__(self, Path):
		self.Separators = [' ', '\n', '\t', '\0', '\r']	
		self.Delimiters = ['+=', '-=', '*=', '/=', ':=', '<>', '<=', '>=', '..','.', ';', ',', '(', ')', '+', '-', '*', '/', '=', '>', '<', '[', ']', ':', '}','{']
		self.Key_words = ['string','integer','shortint','smallint','byte','int64','word','longword','cardinal','uint64','BigInteger',
		'real','double', 'single', 'decimal','boolean', 'char','False','True','and', 'array', 'begin', 'case', 'const', 'do', 'downto',
		'else', 'end','file', 'for', 'foreach', 'function', 'goto', 'if', 'in', 'label', 'mod', 'nil','not', 'of', 'or', 'packed', 
		'procedure', 'program', 'record', 'repeat', 'set', 'then','to', 'type', 'until', 'var', 'while', 'with', 'writeln', 'readln']
		self.curr_symbs = ['','']
		self.input_file = open(Path, 'r')
		self.init_array = False
		self.curr_p = 0
		self.curr_l = 1
		self.lexem_pos = '1:1'
		self.curr_s = ""
		self.current_lexem = ""
#	
#		START
#
	def lex_get(self):
		return self.current_lexem

	def lex_next(self):
		self.current_lexem = self.analyzer()

	def analyzer(self):
		lexem = self.get_lex()
		return lexem		
#
#		MAIN
#
	def get_lex(self):
		buff = Buffer()
		stat = State()
		dict_state = dict_of_states()

		if self.curr_symbs[1] == '':
			self.curr_symbs[1] = self.get_next_symb()

		while True:
			self.get__next()
			
			if stat.get_state() == 1:
				next_state = dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[1]), self.define_symb(self.curr_symbs[0]))
				stat.set_state( next_state  )

			lexem_type = stat.get_state()
			next_state = dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[1]))
			#print('states ', stat.get_state(), '--->' ,next_state, '  ;  symbs ', self.curr_symbs[0],"---> ", self.curr_symbs[1], self.curr_l, self.curr_p, buff.get_buff())

			self.state_action(stat.get_state(),buff)
			
			if stat.get_state() == 7:
				#строка, номер символа и текст сообщения об ошибке
				
				if self.curr_symbs[0] == "":

					str_err = str(self.curr_l) + ":" + str(self.curr_p) + " Unexpected end of file"
					raise ValueError(str_err)
				str_err = str(self.curr_l) + ":" + str(self.curr_p) + " Unexpected symbol " + "'"+ self.curr_symbs[0]+"'"
				raise ValueError(str_err)


# 		ВЫНЕСТИ В ОТДЕЛЬНУЮ ФУНКЦИЮ

			if stat.get_state() == 4 and self.define_symb(self.curr_symbs[0]) == "N" and self.curr_symbs[1] == ".":
				self.get__next()
				if self.define_symb(self.curr_symbs[1]) == "N":
					next_state = 41
					buff.add_buff(self.curr_symbs[0])
				elif self.define_symb(self.curr_symbs[1]) == ".":
					self.init_array = True
					return self.create_lex(buff, 4)
				else:
					next_state = 7
					str_err = str(self.curr_l) + ":" + str(self.curr_p+1) + " Expected number or '.'"
					raise ValueError(str_err)
					#buff.add_buff(self.curr_symbs[0])
#		--->


			stat.set_state( next_state )

			
			#print(lexem_type, self.curr_symbs[0], self.lexem_pos)
			if  stat.get_state() == 1:
				#if lexem_type == 80:
					#buff.clear_buff()
					#self.lexem_pos = -1
				if buff.get_buff() != "":
					if lexem_type == 9:
						if buff.get_buff()[0] == buff.get_buff()[-1] == "'":
							return self.create_lex(buff, 5)
						if buff.get_buff()[0] == "{" and buff.get_buff()[-1] == "}":
							return self.create_lex(buff, 81)
						if not buff.get_buff() in self.Delimiters:
							
							str_err = str(self.curr_l) + ":" + str(self.curr_p) + " Wrong delimiter " + "'"+buff.get_buff()+"'"
							raise ValueError(str_err)
							#stat.set_state(7)
						else:
							return self.create_lex(buff, lexem_type)
					else: 
						return self.create_lex(buff, lexem_type)

			if stat.get_state() == 3:
				if buff.get_buff() == "":
					return self.create_lex(buff, 3)
				else:
					return self.create_lex(buff, dict_state.find_state( 1, self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[0])))

#
#		MAIN
#

	def get_next_symb(self):
		return self.input_file.read(1)

	def get__next(self):
		self.curr_symbs[0] = self.curr_symbs[1]
		self.curr_symbs[1] = self.get_next_symb()
		if self.curr_symbs[0] == '\n':
			 self.curr_l += 1
			 self.curr_p = -1
		self.curr_p += 1
		

	def state_action(self, stat, buff):
		#if stat != 1 and stat != 81 and stat != 80:
		if stat != 1:
			if self.lexem_pos == -1:
				self.lexem_pos = str(self.curr_l) + ':' + str(self.curr_p)

			buff.add_buff(self.curr_symbs[0])
			if self.init_array:
				buff.add_buff(self.curr_symbs[0])
				self.init_array = False
		

	def define_symb(self,symb):
		if symb == "":
			return symb
		elif symb.isalpha():
			if symb == "e":
				return "E"
			elif symb in ['A','B','C','D','E','F']:
				return "D"
			else:
				return "L"
		elif symb.isdigit():
			return "N"
		elif symb in self.Separators:
			if symb == "\n":
				return "\n"
			return "S"
		elif symb == "+" or symb == "*":
			return "I"
		elif symb == ">" or symb == "<":
			return "W"
		else:
			return symb


	def create_lex(self, buff, state):
		value = buff.get_buff()

		if state == 4:
			type_s = 'int'
		elif state == 5:
			type_s = 'string'
			
			unic = value[1:-1]
			if unic.find("'") != -1:
				unic = unic[unic.find("'")+1:unic.rfind("'")]
				if unic == "#10" or unic == "#13" or unic == "#13#10" :
					value = value.replace(unic, "\n")
				elif unic == "#9":
					value = value.replace(unic, "\t")
				else:
					str_err = str(self.curr_l) + ":" + str(self.curr_p) + " Illegal char constant"
					raise ValueError(str_err)

			value = value.replace("'",'')
		elif state == 6:
			if value in self.Key_words:
				type_s = 'reserved id'
			else:
				type_s = 'id'				
		elif state == 9:
			type_s = 'delimiter'
		elif state == 41:
			correct = re.fullmatch('[-]?(?:\d+\.\d+)(?:[e][-]?\d+)?', value)
			if correct:
				type_s = 'float'
				value = float(buff.get_buff())
			else:
				str_err = str(self.curr_l) + ":" + str(self.curr_p) + " Wrong float format"
				raise ValueError(str_err);
		elif state == 2:
			type_s = 'hex'
			try:
				value = hex(int(value.replace('$',"", 1), 16))
			except Exception as e:
				str_err = str(self.curr_l) + ":" + str(self.curr_p) + " invalid symbol for int with base 16"
				raise ValueError(str_err)
		elif state == 11:
			type_s = 'octal'
			try:
				value = oct(int(value.replace('&',"", 1), 8))
			except Exception as e:
				str_err = str(self.curr_l) + ":" + str(self.curr_p) + " invalid symbol for int with base 8"
				raise ValueError(str_err)
		elif state == 12:
			type_s = 'binary'
			try:
				value = bin(int(value.replace('%',"", 1), 2))
			except Exception as e:
				str_err = str(self.curr_l) + ":" + str(self.curr_p) + " invalid symbol for int with base 2"
				raise ValueError(str_err)
			
		elif state == 3:
			type_s = 'eof'
		elif state == 80 or state == 81:
			self.lexem_pos = -1
			buff.clear_buff()
			return self.analyzer()
		else:
			type_s = state
		new_lex = Lexer(self.lexem_pos, type_s, buff.get_buff(), value)


		self.lexem_pos = -1
		buff.clear_buff()
		return new_lex
	