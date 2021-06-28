'''
		1	start
		2	number_16
		3	final
		4	number_int
		41	number_float
		5	string
		6	id
		7	error
		80	one-line comment 
		81  comment
		9	delimit

'''
class dict_of_states:
	def __init__(self):
		self.Dict_state = { 
		1: 	{"L": 6, "D": 6, "E": 6, "N": 4, "S": 1,"$": 2, "I": 9, "-": 9, "/": [9,80], ",": 9,".": 9, ":": 9, ";": 9,
				 "(": 9, ")": 9, "[": 9, "]": 9, "{": 81, "}": 1, "'": 5, "W": 9, "=": 9, "_":  6, "": 3, "\n": 1, "A": 7} ,

		2: 		{"L": 7, "D": 2, "E": 7, "N": 2, "S": 1,"$": 2, "I": 1, "-": 1, "/": 1, ",": 1,".": 7, ":": 7, ";": 1, "(": 7,
				 ")": 3, "[": 7, "]": 7, "{": 1, "}": 7, "'": 7, "W": 1, "=": 1, "_":  7, "": 1, "\n": 1, "A": 7},

		3: 		{"L": 7, "D": 7, "E": 7, "N": 7, "S": 7,"$": 7, "I": 7, "-": 7, "/": 7, ",": 7, ".": 7, ":": 7, ";": 7, "(": 7,
				 ")": 7, "[": 7, "]": 7, "{": 7, "}": 7, "'": 7, "W": 7, "=": 7, "_":  7, "": 3, "\n": 7, "A": 7},

		4: 		{"L": 7, "D": 7, "E": 7, "N": 4, "S": 1,"$": 7, "I": 1, "-": 1, "/": 1, ",": 1, ".": 41, ":": 7, ";": 1,
				 "(": 1, ")": 1, "[": 1, "]": 1, "{": 1, "}": 7, "'": 7, "W": 1, "=": 1, "_":  7, "": 1, "\n": 1, "A": 7},

		41: 	{"L": 7, "D": 7, "E": 41, "N": 41, "S": 1,"$": 7, "I": 1, "-": [41,1], "/": 1, ",": 1,".": 7, ":": 7, ";": 1,
				 "(": 1, ")": 1, "[": 1, "]": 1, "{": 1, "}": 7, "'": 7, "W": 1, "=": 1, "_":  7, "": 1, "\n": 1, "A": 7},

		5: 		{"L": 5, "D": 5, "E": 5, "N": 5, "S": 5,"$": 5, "I": 5, "-": 5, "/": 5, ",": 5,".": 5, ":": 5, ";": 5, "(": 5,
				 ")": 5, "[": 5, "]": 5, "{": 5, "}": 5, "'": 9, "W": 5, "=": 5, "_":  5, "": 1, "\n": 7, "A": 5},

		6: 		{"L": 6, "D": 6, "E": 6, "N": 6, "S": 1,"$": 7, "I": 1, "-": 1, "/": 1, ",": 1,".": 1, ":": 1, ";": 1, "(": 1,
				 ")": 1, "[": 1, "]": 1, "{": 1, "}": 7, "'": 7, "W": 1, "=": 1, "_":  6, "": 1, "\n": 1, "A": 7},

		7: 		{"L": 3, "D": 3, "E": 3, "N": 3, "S": 3,"$": 3, "I": 3, "-": 3, "/": 3, ",": 3,".": 3, ":": 3, ";": 3, "(": 3, ")": 3,
				 "[": 3, "]": 3, "{": 3, "}": 3, "'": 3, "W": 3, "=": 3, "_":  3, "": 3, "\n": 3, "A": 7},

		80:		{"L": 80, "D": 80, "E": 80, "N": 80, "S": 80,"$": 80, "I": 80, "-": 80, "/": 80, ",": 80,".": 80, ":": 80, ";": 80, "(": 80, ")": 80,
				 "[": 80, "]": 80, "{": 80, "}": 80, "'": 80, "W": 80, "=": 80, "_":  80, "": 1, "\n": 1, "A": 80},

		81:		{"L": 81, "D": 81, "E": 81, "N": 81, "S": 81,"$": 81, "I": 81, "-": 81, "/": 81, ",": 81,".": 81, ":": 81, ";": 81, "(": 81, ")": 81,
				 "[": 81, "]": 81, "{": 7, "}": 1, "'": 81, "W": 81, "=": 81, "_":  81, "": 1, "\n": 81, "A": 81}}
		
		self.Dict_state_9 = { 
		"$": 		{"L": 7, "D": 2, "E": 7, "N": 2, "S": 7,"$": 7, "I": 7, "-": 7, "/": 7, ",": 7,".": 7,
		 ":": 7, ";": 7, "(": 7, ")": 7, "[": 7, "]": 7, "{": 7, "}": 7, "'": 7, "W": 7, "=": 7, "_":  7, "": 1, "\n": 7, "A": 7},

		"I": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 1, "I": 7, "-": 7, "/": 7, ",": 7,".": 7, ":": 7, ";": 7,
		 "(": 1, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 1, "W": 7, "=": 9, "_":  1,"": 1, "\n": 1, "A": 7}, 

		"-": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 1, "I": 7, "-": 7, "/": 7, ",": 7,".": 7, ":": 7,
		 ";": 7, "(": 1, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 7, "W": 7, "=": 9, "_":  1, "": 1, "\n": 1, "A": 7}, 

		"/": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 1, "I": 7, "-": 7, "/": 80, ",": 7,".": 7, ":": 7, ";": 7,
		 "(": 1, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 7, "W": 7, "=": 9, "_":  1, "": 1, "\n": 1, "A": 7}, 

		",": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 1, "I": 7, "-": 7, "/": 7, ",": 7,".": 7, ":": 7, ";": 7,
		 "(": 1, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 1, "W": 7, "=": 7, "_":  1, "": 1, "\n": 1, "A": 7}, 

		".": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 7, "I": 7, "-": 7, "/": 7, ",": 7,".": 9, ":": 7,
		 ";": 7, "(": 7, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 7, "W": 7, "=": 7, "_":  1, "": 3, "\n": 1}, 

		":": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 7, "I": 7, "-": 7, "/": 7, ",": 7,".": 7, ":": 7, ";": 7,
		 "(": 7, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 7, "W": 7, "=": 9, "_":  1, "": 1, "\n": 1, "A": 7},

		";": 		{"L": 1, "D": 1, "E": 1, "N": 7, "S": 1,"$": 7, "I": 7, "-": 7, "/": 1, ",": 7,".": 7, ":": 7, ";": 7,
		 "(": 7, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 7, "W": 7, "=": 7, "_":  1, "": 1, "\n": 1, "A": 7}, 

		"(": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 1, "I": 1, "-": 1, "/": 1, ",": 1,".": 1, ":": 1, ";": 1,
		 "(": 1, ")": 1, "[": 1, "]": 1, "{": 1, "}": 1, "'": 1, "W": 1, "=": 1, "_":  1, "": 1, "\n": 1, "A": 7},

		"[": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 1, "I": 1, "-": 1, "/": 1, ",": 1,".": 1, ":": 1, ";": 1,
		 "(": 1, ")": 1, "[": 1, "]": 1, "{": 1, "}": 1, "'": 1, "W": 1, "=": 1, "_":  1, "": 1, "\n": 1, "A": 7},

		"'": 		{"L": 7, "D": 7, "E": 7, "N": 7, "S": 1,"$": 7, "I": 1, "-": 7, "/": 7, ",": 1,".": 7, ":": 7, ";": 1,
		 "(": 7, ")": 1, "[": 7, "]": 7, "{": 1, "}": 7, "'": 7, "W": 1, "=": 1, "_":  7, "": 1, "\n": 1, "A": 7},

		"W": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 1, "I": 7, "-": 7, "/": 7, ",": 7,".": 7, ":": 7, ";": 7,
		 "(": 1, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 1, "W": 9, "=": 9, "_":  1, "": 1, "\n": 1, "A": 7},

		"=": 		{"L": 1, "D": 1, "E": 1, "N": 1, "S": 1,"$": 1, "I": 7, "-": 1, "/": 7, ",": 7,".": 7, ":": 7, ";": 7,
		 "(": 1, ")": 7, "[": 7, "]": 7, "{": 1, "}": 7, "'": 1, "W": 7, "=": 7, "_":  1, "": 1, "\n": 1, "A": 7},

		 ")": 		{"L": 1, "D": 1, "E": 1, "N": 7, "S": 1,"$": 7, "I": 1, "-": 1, "/": 1, ",": 7,".": 7, ":": 1, ";": 1,
		 "(": 7, ")": 1, "[": 7, "]": 1, "{": 1, "}": 7, "'": 7, "W": 1, "=": 1, "_":  1, "": 1, "\n": 1, "A": 7},

		"]": 		{"L": 1, "D": 1, "E": 1, "N": 7, "S": 1,"$": 7, "I": 1, "-": 1, "/": 1, ",": 7,".": 7, ":": 1, ";": 1,
		 "(": 7, ")": 1, "[": 7, "]": 7, "{": 1, "}": 7, "'": 7, "W": 1, "=": 1, "_":  1, "": 1, "\n": 1, "A": 7}}
	
	def find_state(self,curr_state,curr_symb,next_symb):
		#print(curr_state,curr_symb,next_symb)

		if not next_symb in self.Dict_state[1]:
			next_symb = "A"

		if not curr_symb in self.Dict_state[1]:
			curr_symb = "A"
		
		return self.choose_state(curr_state,curr_symb,next_symb)


	def choose_state (self,curr_state,curr_symb,next_symb):
		if curr_state == 9:
			if type(self.Dict_state_9[curr_symb][next_symb]) is list:
				return self.Dict_state_9[curr_symb][next_symb][0]
			return self.Dict_state_9[curr_symb][next_symb]
		
		if type(self.Dict_state[curr_state][next_symb]) is list:
			if curr_state == 41:
				if curr_symb == "E":
					return 41
				else:
					return 1
			else:
				return self.Dict_state[curr_state][next_symb][0]
		else:
			return self.Dict_state[curr_state][next_symb]

