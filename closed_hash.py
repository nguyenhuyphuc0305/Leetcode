# Closed Hash Table with Linear Probing

class ClosedHash:
    def __init__(self,n):
        self.size = n
        self.arr = [-1] * self.size
    def __str__(self):
        res = ""
        for i in range(self.size):
            if self.arr[i] == -1 or self.arr[i] == None:
                res += "Row " + str(i) + " None\n"
            else: 
                res += "Row " + str(i) + " " + str(self.arr[i]) + "\n"
        return res
    def hash(self,i):
        return (i % self.size)
    def rehash(self,i,k):
        return ((self.hash(i) + k) % self.size)
    def insert(self,num):
        k = 0
        while True:
            index = self.rehash(num,k)
            if self.arr[index] == -1 or self.arr[index] == None:
                self.arr[index] = num
                break
            else:
                if self.arr[index] == num:
                    return
                k = k + 1
    def member(self,num):
        k = 0
        while True:
            index = self.rehash(num,k)
            if self.arr[index] == -1 or k >= self.size:
                return False
            elif self.arr[index] == num:
                return True
            else:
                k = k + 1
        return
    def delete(self,num):
        k = 0
        while True:
            index = self.rehash(num,k)
            if self.arr[index] == -1 or k >= self.size:
                return
            elif self.arr[index] == num:
                self.arr[index] = None
                return
            else:
                k = k + 1
            

# ##### TEST #####

hashTable = ClosedHash(7)
hashTable.insert(6)
hashTable.insert(32)
hashTable.insert(34)
hashTable.insert(3)
hashTable.insert(12)
hashTable.insert(24)
hashTable.insert(35)
hashTable.delete(1)
print(hashTable)