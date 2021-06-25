from simple_parser import *
from analyzation1 import *
from expr_node import *
class test_parser():

	def __init__(self):
		self.space = 20
		self.strr = ""
		self.main()


	def main(self):
		count = 0
		for i in range(1,36):
			print("_____________TEST №", i,"_____________")

			test_prog = "tests_parser\\test"+str(i)+".txt"
			
			self.printBinOpNode(simple_parser(test_prog).parseExp(),2)

			with open("result.txt", "a") as f:
				f.write(self.strr)

			with open("result.txt", "r") as f:
				result = f.read()

			with open("tests_parser\\test"+str(i)+"_res.txt", "r") as f:
				test_result = f.read()
			
			#print(result)
			#print('______________________________')
			#print(test_result)
			if result == test_result:
				print('OK')
				count += 1
			else:
				print('WRONG')
			with open("result.txt", "w") as f:
				f = ""
			self.strr = ""
			self.space = 20
			
		print('Всего пройдено тестов ' + str(count) + '/35')

	

	def printBinOpNode(self, node, field):
		#print("%5s%5s%5s" % (node.getLeftNode().getValue(), node.getValue(), node.getRightNode().getValue()) + "\n")
		self.strr+=( " ".center(field*2) + node.getValue().get_value().center(field)+"\n")
		
		#self.strr+=(" "*self.space + node.getValue().get_value()+"\n")
		#print(" "*self.space + node.getValue().get_value()+"\n")
		if node.getValue().get_type() == 'error':
			err_symb =  node.getValue().get_value()
			if err_symb == "":
				err_symb = "eof"
			self.strr+=(str(node.getValue().get_pos())+ ' Error: Unexpected symbol '+ err_symb)
			
			return
		if node.getLeftNode():

			self.printBinOpNode(node.getLeftNode(), field+2)
			
		if node.getRightNode():
			self.printBinOpNode(node.getRightNode(), field+2)
		self.space = self.space + 2

		
	def printBinOpNode1(self, node):
		#print("%5s%5s%5s" % (node.getLeftNode().getValue(), node.getValue(), node.getRightNode().getValue()) + "\n")
		self.strr+=(" "*self.space + node.getValue().get_value().center(self.space)+"\n")
		#self.strr+=(" "*self.space + node.getValue().get_value()+"\n")
		#print(" "*self.space + node.getValue().get_value()+"\n")
		if node.getValue().get_type() == 'error':
			err_symb =  node.getValue().get_value()
			if err_symb == "":
				err_symb = "eof"
			self.strr+=(node.getValue().get_pos(), 'Error: Unexpected symbol', err_symb)
			return
		if node.getLeftNode():
			self.space = self.space - 2
			self.printBinOpNode(node.getLeftNode())
			
		if node.getRightNode():
			
			self.printBinOpNode(node.getRightNode())
			self.space = self.space + 2
		self.space = self.space + 2
