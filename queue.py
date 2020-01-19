class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next
    def __str__(self):
        return ("%d" %(self.value))
    def getNext(self):
        return self.next
    def setNext(self,n):
        self.next = n
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v

class Queue:
    def __init__(self):
       self.first = None
       self.last = None
    def __str__(self):
        if self.first == None:
            return "Queue Empty"
        else:
            cur = self.first
            res = ""
            while cur != None:
                res += cur.__str__() + " "
                cur = cur.next
        return res
        
    def front(self):
        return self.first
    def empty(self):
        if self.first == None:
            return True
        else:
            return False 
    def enqueue(self,x):
        if self.empty():
            self.first = Node(x,None)
            self.last = self.first
        else:
            self.last.setNext(Node(x,None))
            self.last = self.last.next
    def dequeue(self):
        res = self.first.value
        if not self.empty():
            self.first = self.first.next
        return res


print("The Josephus Problem")
n_people = int(input("Enter the Number of People in the Group:\n"))
m_th = int(input("Enter value for Mth Person to be killed:\n"))

q = Queue()
for i in range(n_people):
    q.enqueue(i)

res = ""
count = 1
while not q.empty():
    if count != m_th:
        temp = q.dequeue()
        q.enqueue(temp)
        count += 1

    else:
        temp = q.dequeue()
        res += str(temp) + " "
        count = 1