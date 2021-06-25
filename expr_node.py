from Node import Node


class IntegerNode(Node):
	def __init__(self, number):
		Node.__init__(self, None, None, number)
#
#
#

class IdNode(Node):
	def __init__(self, idNode):
		Node.__init__(self, None, None, idNode)
#
#
#

class BinOpNode(Node):
	def __init__(self, leftNode, rightNode, opType):
		Node.__init__(self, leftNode, rightNode, opType)
		