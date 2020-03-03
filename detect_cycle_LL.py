# Problem: Given a linked list, detect if there is a cycle or not. If yes, return the node where last node points to. If no, return None
#   4 -> 7 -> 8 -> 0 -> 1 -> 6
#             <---------------
# Idea: Using Floyd's Tortoise and Hare Algorithm
# If only ask for there is cycle or not, we can stop at meet 2

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        res = ""
        cur = self
        if cur == None:
            return "Empty"
        while cur != None:
            res = res + str(cur.val) + " "
            cur = cur.next
        return res

def detect_pos(head):
    if head == None:
        return None
    slow, fast = head, head
    meet = 0
    while fast != None and fast.next != None:
        if slow == fast:
            meet = meet + 1
            if meet == 2:
                if slow == head:
                    return head.val
                else:
                    slow = head
        if meet == 1:
            slow = slow.next
            fast = fast.next.next
        elif meet == 2:
            slow = slow.next
            fast = fast.next
        elif meet == 3:
            return slow.val
    return None

##### TEST #####
# head = Node(4, Node(7, Node(8, Node(0, Node(1, Node(6))))))
# head.next.next.next.next.next.next = head.next.next.next
# print(detect_pos(head))