from analyzation1 import *
class test:
	def __init__(self):
		self.check()

	def check(self):

		for i in range(1,10):
			print("_____________TEST №", i,"_____________")
			test_prog = "tests\\test"+str(i)+".txt"
			
			analyz = analyzation(test_prog)
			while True:
				lexem = analyz.analyzer()
				with open("result.txt", "a") as f:
					f.write("%5d%16s%16s%16s" % (lexem.get_pos(), str(lexem.get_type()),str(lexem.get_orig()), str(lexem.get_value()) + '\n'))
				if  lexem.get_type() == 'eof':
					break

			with open("result.txt", "r") as f:
				result = f.read()
			with open("tests\\res"+str(i)+".txt", "r") as f:
				test_result = f.read()
			
			#print(result)
			if result == test_result:
				print('OK')
			else:
				print('WRONG')


			with open("result.txt", "w") as f:
				f = ""

			

