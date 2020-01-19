class Node:
    def __init__(self, payload: int):
        self.payload = payload
        self.next = None


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def __str__(self):
        current = self.head
        result = ""
        while (current != None):
            if (current.next != None):
                result += (str(current.payload) + " -> ")
            else:
                result += (str(current.payload) + " -> NULL")
            current = current.next
        return result

    def size(self):
        current = self.head
        result = 0
        while (current != None):
            result += 1
            current = current.next
        return result

    def get(self, index: int):
        count = 0
        current = self.head
        while (current != None):
            if count == index:
                return current.payload
            count += 1
            current = current.next
        return -1

    # Insert the node to specify index of the linked list. If index == length of list then append it to the end else invalid index
    def insert(self, index: int, payload: int):
        previous = None
        current = self.head
        count = 0
        newNode = Node(payload)

        if index == self.size():
            return self.addEnd(payload)
        while (current != None):
            if count == index:
                if previous != None:
                    newNode.next = current
                    previous.next = newNode
                    return self
                else:
                    return self.addFront(payload)
            count += 1
            previous = current
            current = current.next
        return ("Invalid index")

    def delete(self, index):
        count = 0
        current = self.head
        previous = None

        while (current != None):
            if count == index:
                if previous != None:
                    previous.next = current.next
                    return self
                else:
                    return LinkedList(self.head.next)
            count += 1
            previous = current
            current = current.next
        return ("Invalid index")

    def search(self, target: int):
        current = self.head
        while (current != None):
            if (current.payload == target):
                return "Found " + str(target)
            current = current.next
        return "Not found " + str(target)

    def addFront(self, payload: int):
        needAdd = Node(payload)
        needAdd.next = self.head

        return LinkedList(needAdd)

    def addEnd(self, payload: int):
        needAdd = Node(payload)
        current = self.head

        if current == None:
            return LinkedList(needAdd)
        while (current.next != None):
            current = current.next
        current.next = needAdd
        return LinkedList(self.head)

    def reverse(self):
        previous, current, next = None, self.head, self.head
        while (current != None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        result = LinkedList()
        result.head = previous
        return result

    # add 2 linked list, which each node's payload is a digits, and return a linked list
    # Notes: the number is reverse
    # eg: 1 -> 2 -> 3 is 321

    def addNum(self, target):
        current1, current2 = self.head, target.head
        carry = 0
        result = LinkedList()

        while ((current1 != None) or (current2 != None)):
            if (current1 == None):
                current1Val = 0
            else:
                current1Val = current1.payload
            if (current2 == None):
                current2Val = 0
            else:
                current2Val = current2.payload
            sumVal = current1Val + current2Val + carry
            data = sumVal % 10
            carry = sumVal // 10
            result = result.addEnd(data)
            if (current1 != None):
                current1 = current1.next
            if (current2 != None):
                current2 = current2.next
        return result


ll = LinkedList()
ll = ll.addFront(5)
ll = ll.addEnd(2)
ll = ll.addFront(8)

print(ll)
print(ll.delete(3))
