import math
class heap:
	def __init__(self):
		self.data = []
		self.res = ""
	def __str__(self):
		res=""
		for x in self.data:
			res=res+str(x)+" "
		return res
	def makenull(self):
		self.data = []
	def insert(self,x):
		self.data.append(x)
		self.upheap(len(self.data) - 1)
	def parent(self,index):
		return math.floor((index - 1) / 2)
	def left(self,index):
		return (2 * index + 1)
	def right(self,index):
		return (2 * index + 2)
	def swap(self,a,b):
		self.data[a] , self.data[b] = self.data[b], self.data[a]
	def upheap(self,index):
		if (self.parent(index) < 0):
			return
		if self.data[self.parent(index)] <= self.data[index]:
			return
		self.swap(index, self.parent(index))
		self.upheap(self.parent(index))
	def inorder(self,index):
		self.res = ""
		def inorderChild(ind):
			if ind >= len(self.data):
				return
			else:
				inorderChild(self.left(ind))
				self.res = self.res + str(self.data[ind]) + " "
				inorderChild(self.right(ind))
		inorderChild(index)
		return self.res
		
	def preorder(self,index):
		self.res = ""
		def preorderChild(ind):
			if ind >= len(self.data):
				return
			else:
				self.res = self.res + str(self.data[ind]) + " "
				preorderChild(self.left(ind))
				preorderChild(self.right(ind))
		preorderChild(index)
		return self.res

	def postorder(self,index):
		self.res = ""
		def postorderChild(ind):
			if ind >= len(self.data):
				return
			else:
				postorderChild(self.left(ind))
				postorderChild(self.right(ind))
				self.res = self.res + str(self.data[ind]) + " "
		postorderChild(index)
		return self.res

	def min(self):
		return self.data[0]
	def deletemin(self):
		self.swap(0, len(self.data) - 1)
		self.data.pop()
		self.downheap(0)
	def downheap(self,index):
		if not self.data:
			return
		if (self.left(index) >= len(self.data) and (self.right(index) >= len(self.data))):
			return
		
		if (self.right(index) >= len(self.data)):
			if (self.data[index] > self.data[self.left(index)]):
				self.swap(index, self.left(index))
				self.downheap(self.left(index))
			else:
				return
		else:
			if (self.data[index] <= self.data[self.left(index)]) and (self.data[index] <= self.data[self.right(index)]):
				return
			if self.data[self.left(index)] <= self.data[self.right(index)]:
				self.swap(index, self.left(index))
				self.downheap(self.left(index))
			else:
				self.swap(index, self.right(index))
				self.downheap(self.right(index))
	def sort(self):
		tempData = self.data[:]
		while self.data:
			print(self.min())
			self.deletemin()
		self.data = tempData[:]

##### TEST ZONE #####

myHeap = heap()
myHeap.insert(5)
myHeap.insert(7)
myHeap.insert(4)
myHeap.insert(2)
myHeap.insert(1)
myHeap.insert(3)
myHeap.insert(8)
myHeap.insert(10)
myHeap.insert(9)
myHeap.insert(6)

print(myHeap)
print(myHeap.inorder(0))

print(myHeap.preorder(0))

print(myHeap.postorder(0))