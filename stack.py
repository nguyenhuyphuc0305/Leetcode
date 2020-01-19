class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next
    def __str__(self):
        return ("[ %d ]" %(self.value))
    def getNext(self):
        return self.next
    def setNext(self,n):
        self.next = n
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v
        
class Stack:
    def __init__(self):
        self.head = None
    def __str__(self):
        if self.empty():
            return "Stack Empty"
        else:
            cur = self.head
            res = ''
            while cur != None:
                res += cur.__str__()
                cur = cur.next
            return res

    def top(self):
        return self.head.value
    def pop(self):
        if not self.empty():
            temp = self.head.next
            self.head.next = None
            self.head = temp
    
    def push(self,x):
        newNode = Node(x,self.head)
        self.head = newNode
        
    def empty(self):
        if self.head == None:
            return True
        else:
            return False

# s = Stack()
# s.push(1)
# s.push(2)
# s.pop()
# s.pop()
# s.pop()

# print(s)