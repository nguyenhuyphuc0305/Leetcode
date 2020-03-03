# Open Hash Table (or Chaining) implemented below is an array of linked list. Each value will be stored in a Node and when collision happens, they will be 
# appended to the end of the list (append to the front could be way better but Zybook forces me to append to the tail). No duplicate value is allowed
#           Index       Value
#             0           10 -> None           
#             1           -1
#             2           -1
#             3           33 -> None
#             4           14 -> 54 -> None
#             5           -1
#             6           -1
#             7           -1
#             8           -1
#             9           -1

class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    def __str__(self):
        res = ""
        cur = self
        while cur != None:
            res += str(cur.value) + ", "
            cur = cur.getNext()
        return res[:-2]
    def getNext(self):
        return self.next
    def setNext(self,n):
        self.next = n
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v

class OpenHash:
    def __init__(self,n):
        self.size = n
        self.arr = [-1] * self.size 
    def __str__(self):
        res = ""
        for i in range(self.size):
            if self.arr[i] == -1 or self.arr[i] == None:
                res += "Row " + str(i) + " []\n"
            else: 
                res += "Row " + str(i) + " [" + str(self.arr[i]) + "]\n"
        return res

    def hash(self,i):
        return (i%self.size)
    def insert(self,num):
        index = self.hash(num)
        if self.arr[index] == -1 or self.arr[index] == None:
            self.arr[index] = Node(num)
        else:
            cur = self.arr[index]
            if cur.value == num:
                return
            while cur.next != None:
                cur = cur.getNext()
                if cur.value == num:
                    return                
            cur.next = Node(num)
    def member(self,num):
        index = self.hash(num)
        if self.arr[index] == -1 or self.arr[index] == None:
            return False
        else:
            cur = self.arr[index]
            while cur != None:
                if cur.value == num:
                    return True
                cur = cur.getNext()
            return False
    def delete(self,num):
        index = self.hash(num)
        if self.arr[index] == -1 or self.arr[index] == None:
            pass
        elif self.arr[index].value == num:
            self.arr[index] = self.arr[index].getNext()
        else:
            prev, cur = self.arr[index], self.arr[index]
            while cur != None:
                if cur.val == num:
                    prev.setNext(cur.getNext())
                    cur.setNext(None)
                    break
                prev = cur
                cur = cur.getNext()


###### TEST ######
print("Welcome to Open Hash Table Tests")
numRow = int(input("How big would you like your hash table to be?\n"))

hashTable = OpenHash(numRow)
hashTable.insert(9)
hashTable.insert(9)
hashTable.insert(71)
print(hashTable)