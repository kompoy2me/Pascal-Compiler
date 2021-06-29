from simple_parser import *
from analyzation1 import *
from expr_node import *
import traceback
import sys
class tester:
	def __init__(self, test_type):
		self.test_type = test_type
		self.check()

	def check(self):
		count = 0
		for i in range(1,40):#заменить на переменную



			print("_____________TEST №", i, "_____________")
			
			test_prog = "tests_"+self.test_type+"\\test"+str(i)+".txt"
			test_res = "tests_"+self.test_type+"\\test"+str(i)+"_res.txt"
			
			if self.test_type == 'lexer':
				self.write_lex(test_prog)
			elif self.test_type == 'parser':
				self.write_pars(test_prog)
			else:
				print('No such module')
				return

			with open(test_prog, "r") as f:
				test = f.read()


			with open("result.txt", "r") as f:
				result = f.read()

			with open(test_res, "r") as f:
				test_result = f.read()

			print(test)
			print(result) #результат теста
			#print('----------------->')
			#print(test_result) #ответ

			if result == test_result:
				print('OK')
				count += 1
			else:
				print('WRONG')

			with open("result.txt", "w") as f:
				f = ""

		print('Всего пройдено тестов ' + str(count) + '/' + str(i))
#
#
#
	def write_lex(self, test_prog):
		analyz = analyzation(test_prog)

		while True:
			try:
				lexem = analyz.analyzer()
			except Exception as e:
				etype, evalue, tb = sys.exc_info()
				with open("result.txt", "w") as f:
					f.close
				with open("result.txt", "w") as f:
					f.write('{}: {}'.format(etype.__name__, evalue))
				break
			else:
				with open("result.txt", "a") as f:
					f.write("%5s%16s%16s%16s" % (lexem.get_pos(), str(lexem.get_type()),str(lexem.get_orig()), str(lexem.get_value()) + '\n'))
					if  lexem.get_type() == 'eof':
						break
			finally:
				pass
#
#
#
	def write_pars(self, test_prog):

		try:
			simplee_parser = simple_parser(test_prog).parseExp()
			self.printBinOpNode(simplee_parser,2)
		except Exception as e:
			#print(traceback.format_exc())
			#print(traceback.format_exception_only(type(e), e))
			etype, evalue, tb = sys.exc_info()
			with open("result.txt", "a") as f:
				f.write('{}: {}'.format(etype.__name__, evalue))
			
		else:
			pass
		finally:
			pass
#
#
#
	def printBinOpNode(self, node, field):
		with open("result.txt", "a") as f:
			f.write(( " ".center(field*2) + node.getValue().get_value().center(field)+"\n"))
		#self.res_str+=( " ".center(field*2) + node.getValue().get_value().center(field)+"\n")
		if node.getLeftNode():
			self.printBinOpNode(node.getLeftNode(), field+2)
			
		if node.getRightNode():
			self.printBinOpNode(node.getRightNode(), field+2)