from analyzation1 import *
import traceback
class test:
	def __init__(self):
		self.check()

	def check(self):
		count = 0
		for i in range(1,23):
			print("_____________TEST №", i,"_____________")
			test_prog = "tests\\test"+str(i)+".txt"
			
			analyz = analyzation(test_prog)
			
			while True:
				try:
					lexem = analyz.analyzer()
					
				except ValueError as e:
					print(traceback.format_exc())
					break
				except NameError as e:
					print(traceback.format_exc())
					break
				else:
					with open("result.txt", "a") as f:
						f.write("%5s%16s%16s%16s" % (lexem.get_pos(), str(lexem.get_type()),str(lexem.get_orig()), str(lexem.get_value()) + '\n'))
						if  lexem.get_type() == 'eof':
							break
				finally:
					pass
				
				
			with open("result.txt", "r") as f:
				result = f.read()
			with open("tests\\test"+str(i)+"_res.txt", "r") as f:
				test_result = f.read()
			
			print(result)
			if result == test_result:
				print('OK')
				count += 1
			else:
				print('WRONG')
				'''for i in range(0,len(test_result)-1):
					if result[i] != test_result[i]:
						print('position')
						print(i, test_result[i], result[i])
					break'''


			with open("result.txt", "w") as f:
				f = ""
		print('Всего пройдено тестов ' + str(count) + '/22')