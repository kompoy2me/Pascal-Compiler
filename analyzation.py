from Lexer import Lexer
from Buffer import Buffer
from State import State
from dict_of_states import dict_of_states

class analyzation:
	def __init__(self, Path):
		self.Separators = [' ', '\n', '\t', '\0', '\r']	
		self.Lexems_arr = []
		self.curr_symbs = ['','']
		self.read_file(Path)
		self.text 
		self.curr_p
		self.curr_s = ""

		
	def read_file(self, Path):
		with open(Path, "r") as f:
			self.text = f.read()
		self.analyzation()

	'''def get_next(self):
		if self.curr_p < (len(self.text)-1):
			self.curr_p += 1
			self.curr_s = self.text[self.curr_p]
		return self.curr_s'''

	def get_next(self):
		if self.curr_p < (len(self.text)-2):
			self.curr_p += 1
			self.curr_symbs[0] = self.curr_symbs[1]
			self.curr_symbs[1] = self.text[self.curr_p+1]

		
	def state_act(self, stat, buff, next_state):

		if stat == 4 or stat == 5 or stat == 6 or stat == 9 or stat == 41:
			buff.add_buff(self.curr_symbs[0])

		#print("buff ", buff.get_buff(), " next state ", next_state)
		if  buff.get_buff() == "-" and next_state == 4:
			list_d = ["+", "*", "-", "/", ",", "(", "[", ">", "<", ":=", "-=", "+=", "*=", "/="] 
			#print("last lexem", self.Lexems_arr[-1].get_orig())
			if not (self.Lexems_arr[-1].get_orig() in list_d):
				self.Lexems_arr.append(Lexer(self.curr_p - len(buff.get_buff())+1, "минус", buff.get_buff(), "имя"))
				buff.clear_buff()


		if next_state == 1 or stat == 3:
			if stat == 4:
				type_s = 'число'
			elif stat == 5:
				type_s = 'строка'
			elif stat == 6:
				type_s = 'идентификатор'
			elif stat == 9:
				type_s = 'знак'
			else:
				type_s = stat


			new_lex = buff.get_buff()
			if new_lex != "":
				self.Lexems_arr.append(Lexer(self.curr_p - len(new_lex)+1, type_s, new_lex, "имя"))
				buff.clear_buff()


	def define_symb(self,symb):
		if symb.isalpha():
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


	def analyzation(self):
		buff = Buffer()
		stat = State()
		dict_state = dict_of_states()

		self.curr_p = -1
		self.curr_symbs[1] = self.text[0]

		while stat.get_state()!=3:

			self.get_next()
			print(self.curr_p,'  ', self.curr_symbs[0], self.define_symb(self.curr_symbs[0]), stat.get_state() )

			if stat.get_state() == 1:
				next_state = dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[0]))
				self.state_act(stat.get_state(),buff, next_state )
				stat.set_state( next_state  )
				print('->' ,stat.get_state())

			next_state = dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[1]))
			print("BUFFER",buff.get_buff())
			self.state_act(stat.get_state(),buff, next_state)
			
			stat.set_state( next_state )
			print('->' ,stat.get_state())
		
		self.state_act(stat.get_state(),buff, 3)

		for i in range(len(self.Lexems_arr)):
			print(self.Lexems_arr[i].get())


	#текущий символ и следующий символ: для всех элемнтов начиная с позиции 1: 

	'''def analyzation_rec(self,stat,buff,dict_state):
		if stat.get_state() == 3:
			return
		else:
			while stat.get_state()!=3:
				self.get_next()
				print(self.curr_p,'  ', self.curr_symbs[0], self.define_symb(self.curr_symbs[0]), stat.get_state() )

				if stat.get_state() == 1:
					self.state_act(stat.get_state(),buff)
					stat.set_state( dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[0]) ) )
					print('->' ,stat.get_state())

				if stat.get_state() == 'N':
					stat.set_state(1) 
					print('-> 1')
					self.analyzation_rec(stat,buff,dict_state)
					stat.set_state(1) 



				self.state_act(stat.get_state(),buff)

				stat.set_state( dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[1]) ) )
				print('->' ,stat.get_state())'''




	'''def analyzation(self):
		buff = Buffer()
		stat = State()
		dict_state = dict_of_states()

		self.curr_p = -1
		self.curr_symbs[1] = self.text[0]

		while stat.get_state()!=3:

			self.get_next()
			print(self.curr_p,'  ', self.curr_symbs[0], self.define_symb(self.curr_symbs[0]), stat.get_state() )

			if stat.get_state() == 1:
				self.state_act(stat.get_state(),buff)
				stat.set_state( dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[0]) ) )
				print('->' ,stat.get_state())

			self.state_act(stat.get_state(),buff)

			stat.set_state( dict_state.find_state( stat.get_state(), self.define_symb(self.curr_symbs[0]), self.define_symb(self.curr_symbs[1]) ) )
			print('->' ,stat.get_state())
		
		for i in range(len(self.Lexems_arr)-1):
			print(self.Lexems_arr[i].get())








		self.curr_p = -1

		while stat.get_state()!=3:

			if self.curr_p == (len(self.text)-1):
				stat.set_state(3)


			self.get_next()
			stat.set_state(dict_state.find_state(stat.get_state(),self.define_symb(self.curr_s),self.define_symb(self.text[self.curr_p-1])))
			self.state_act(stat.get_state(),buff)
			print(self.curr_p, self.curr_s, self.define_symb(self.curr_s), stat.get_state() )

			
		for i in range(len(self.Lexems_arr)-1):
			print(self.Lexems_arr[i].get())
		self.curr_p = -1

		while self.curr_p < (len(self.text)-1):
			print(self.get_next(),self.curr_p,self.define_symb(self.curr_s))
		print(self.text)


		if stat == 1:
			new_lex = buff.get_buff()
			if new_lex != "":
				self.Lexems_arr.append(Lexer(self.curr_p - len(new_lex), "тип", new_lex, "имя"))
				buff.clear_buff()
		elif stat == 2:
			buff.add_buff(self.curr_symbs[0])

		elif stat== 3:
			new_lex = buff.get_buff()
			if new_lex != "":
				self.Lexems_arr.append(Lexer(self.curr_p - len(new_lex)+1, "тип", new_lex, "имя"))
				buff.clear_buff()
			print('EOF')

		elif stat == 4:
			buff.add_buff(self.curr_symbs[0])
			if next_state == 1:
				new_lex = buff.get_buff()
				if new_lex != "":
					self.Lexems_arr.append(Lexer(self.curr_p - len(new_lex)+1, 'число', new_lex, "имя"))
					buff.clear_buff()

		elif stat == 5:
			buff.add_buff(self.curr_symbs[0])
			if next_state == 1:
				new_lex = buff.get_buff()
				if new_lex != "":
					self.Lexems_arr.append(Lexer(self.curr_p - len(new_lex)+1, 'строка', new_lex, "имя"))
					buff.clear_buff()
		elif stat == 6:
			buff.add_buff(self.curr_symbs[0])
			if next_state == 1:
				new_lex = buff.get_buff()
				if new_lex != "":
					self.Lexems_arr.append(Lexer(self.curr_p - len(new_lex)+1, 'идентификатор', new_lex, "имя"))
					buff.clear_buff()
		elif stat == 7:
			buff.add_buff(self.curr_symbs[0])
		elif stat == 8:
			buff.add_buff(self.curr_symbs[0])
		elif stat == 9:
			buff.add_buff(self.curr_symbs[0])
			if next_state == 1:
				new_lex = buff.get_buff()
				if new_lex != "":
					self.Lexems_arr.append(Lexer(self.curr_p - len(new_lex)+1, 'знак', new_lex, "имя"))
					buff.clear_buff()
		else:
			print('что-то пошло не так')'''
