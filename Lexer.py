class Lexer:
	def __init__(self, pos, type_of, origin, value):
		self.pos = pos
		self.type_of = type_of
		self.origin = origin
		self.value = value

	def get(self):
		return self.pos, self.type_of, self.origin, self.value

	def get_pos(self):
		return self.pos

	def get_type(self):
		return self.type_of

	def get_orig(self):
		return self.origin

	def get_value(self):
		return self.value
	