class State:
	def __init__(self):
		self.State = 1
		#self.States = ['start', 'string', 'numb16', 'numb', 'delimit', 'final', 'ident', 'error', 'double_del', 'comment']

	def set_state(self, state):
		#if state in self.States:
		self.State = state

	def get_state(self):
		return self.State