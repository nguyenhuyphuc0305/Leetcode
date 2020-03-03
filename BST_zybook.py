class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self == None:
            return "None"
        res = "Val: " + str(self.val) + ", Left: "
        if self.left == None:
            res = res + "None, Right: "
        else:
            res = res + str(self.left.val) + ", Right: "
        if self.right == None:
            res = res + "None"
        else:
            res = res + str(self.right.val)
        return res
        

class BST:
    def __init__(self):
        self.root = None
    def __str__(self):
        if self.root == None:
            return "Empty Tree"
        res = ["","",""]

        def inOrder(head):
            if head == None:
                res[0] = res[0] + "N "
            else:
                res[0] = res[0] + str(head.val) + " "
                inOrder(head.left)
                inOrder(head.right)

        def preOrder(head):
            if head == None:
                res[1] = res[1] + "N "
            else:
                preOrder(head.left)
                res[1] = res[1] + str(head.val) + " "
                preOrder(head.right)

        def postOrder(head):
            if head == None:
                res[2] = res[2] + "N "
            else:
                postOrder(head.left)
                postOrder(head.right)
                res[2] = res[2] + str(head.val) + " "
        
        inOrder(self.root)
        preOrder(self.root)
        postOrder(self.root)
        return ("Preorder: " + res[0] + "\b\nInorder: " + res[1] + "\b\nPostorder: " + res[2])

    def insert(self,x):
        if self.find(x):
            return
        if self.root == None:
            self.root = Node(x)
            return
        cur = self.root
        parent = None
        while cur != None:
            parent = cur
            if x > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        if x > parent.val:
            parent.right = Node(x)
        else:
            parent.left = Node(x)
    def find(self,x):
        cur = self.root
        while cur != None:
            if cur.val == x:
                return True
            elif cur.val < x:
                cur = cur.right
            else:
                cur = cur.left
        return False


##### TEST #####
bst = BST()
bst.insert(6)
bst.insert(8)
bst.insert(4)
bst.insert(3)
bst.insert(7)
bst.insert(5)
bst.insert(9)

print(bst)