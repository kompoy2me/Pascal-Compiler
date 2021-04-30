class Buffer:
	def __init__(self):
		self.Buffer = ''
		
	def clear_buff(self):
		self.Buffer = ''
		
	def add_buff(self, symb):
		self.Buffer += symb

	def get_buff(self):
		return self.Buffer