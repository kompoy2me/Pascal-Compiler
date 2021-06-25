class Node:
	def __init__(self, leftNode, rightNode, value):
		self.value = value
		self.leftNode = leftNode
		self.rightNode = rightNode

	def getLeftNode(self):
		return self.leftNode

	def getRightNode(self):
		return self.rightNode
	
	def getValue(self):
		return self.value
