##Implement the node delete function in the programming language of your choice based on the template provided

class NODE(object):
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class LIST(object):
	def __init__(self):
		self.head = None
		self.tail = None

		
	def BEFOREDELETION(self):
		node = self.head
		while node != None:
			print('Nodes given : ',node.data)
			node = node.next


	def DELETEFUNCTION(self, node):
		if node.previous != None:
			node.previous.next = node.next
		else:
			self.head = node.next
		if node.next != None:
			node.next.previous = node.next
		else:
			self.tail = node.previous
		
	def AFTERDELETION(self):
		node = self.head
		while node != None:
			print('Nodes After deletion: ',node.data)
			node = node.next
			
	def INSERTNOTE(self, node, x):
		if node != None:
			x.next = node.next
			node.next = x
			x.previous = node
			if x.next != None:
				x.next.previous = x
		if self.head == None:
			self.head = self.tail = x
			x.previous = x.next = None
		elif self.tail == None:
			self.tail = xrange
	

N1 = NODE(18)
N2 = NODE(20)
N3 = NODE(80)
list = LIST()
list.INSERTNOTE(None, N1)
list.INSERTNOTE(list.head, N2)
list.INSERTNOTE(list.head, N3)
list.BEFOREDELETION()
list.DELETEFUNCTION(N1)
list.AFTERDELETION()

