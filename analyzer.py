from Lexer import Lexer
from Buffer import Buffer
from State import State

class analyzer:
	def __init__(self, Path):
		self.Key_words = ['and', 'array', 'begin', 'case', 'const', 'div', 'do', 'downto','else', 'end', 'file', 'for', 'foreach', 'function', 'goto', 'if', 'in', 'label', 'mod', 'nil', 'not', 'of', 'or', 'packed', 'procedure', 'program', 'record', 'repeat', 'set', 'then', 'to', 'type', 'until', 'var', 'while', 'with']
		self.Delimiters = ['.', ';', ',', '(', ')', '+', '-', '*', '/', '=', '>', '<', '[', ']', ':', '}','{']
		self.Double_Del = ['+=', '-=', '*=', '/=', ':=', '<>', '<=', '>=', '..']
		self.Separators = [' ', '\n', '\t', '\0', '\r']		
		self.File = open(Path, 'r')
		self.Current = ""
		self.analysis()
		self.Lexems_arr = []

	def get_next(self):
		#print(self.File.tell())
		return self.File.read(1)

	def get_pos(self):
		return self.File.tell()

	def analysis(self):
		Buff = Buffer()
		Stat = State()
		
		#Buff.add_buff(self.Current)
		#print(Buff.get_buff())
		#print(self.Current)
		self.Current = self.get_next()

		while Stat.get_state() != 'final' :
			
			if Stat.get_state() == 'start':
				
				if self.Current in self.Separators:
					self.Current = self.get_next()

				elif self.Current.isalpha():
					Buff.clear_buff()
					Buff.add_buff(self.Current)
					Stat.set_state('ident')
					self.Current = self.get_next()
					#print(Buff.get_buff())

				elif self.Current.isdigit():
					Buff.clear_buff()
					Buff.add_buff(self.Current)
					Stat.set_state('numb')
					self.Current = self.get_next()

				elif self.Current == '{':
					#ЗАПИСАТЬ КОММЕНТАРИЙ В БУФЕР
					Stat.set_state('comment')
					self.Current = self.get_next()

				elif self.Current == '.':
					Lexems_arr.append(Lexer.Lexer(self.get_pos(), 'Разделитель', self.Current, 'имя'))
					Stat.set_state('final')

				elif self.Current in self.Delimiters:
					Stat.set_state('delimit')
					self.Current = self.get_next()

					








