# A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. 
# Major operation: make_set
#                  find (determine which subset an element belongs)
#                  union (join 2 subset into 1)
# I will use union by weight

class Disjoint:
    # init arr of num_nodes with all weight -1
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.arr = [-1 for elem in range(num_nodes)]

    # find the root of the sub-tree that has negative weight
    def find_root(self, index):
        res = index
        while self.arr[res] >= 0:
            res = self.arr[res]
        return res

    # Join 2 set, the one with lower weight (more nodes) will be parents, no path compression
    def union(self, index1, index2):
        root1 = self.find_root(index1)
        root2 = self.find_root(index2)

        if root1 == root2:
            return
        if self.arr[root1] <= self.arr[root2]:
            self.arr[root1] = self.arr[root1] + self.arr[root2]
            self.arr[root2] = root1
        else:
            self.arr[root2] = self.arr[root1] + self.arr[root2]
            self.arr[root1] = root2



############### TEST ###############
if __name__ == "__main__":
    a = Disjoint(6)
    a.union(0,2)
    print(a.arr)
    a.union(3,5)
    print(a.arr)
    a.union(1,4)
    print(a.arr)
    a.union(2,5)
    print(a.arr)
    a.union(0,3)
    print(a.arr)
    a.union(2,3)
    print(a.arr)
    a.union(2,1)
    print(a.arr)
    a.union(0,1)
    print(a.arr)
    a.union(2,4)
    print(a.arr)
    a.union(4,5)
    print(a.arr)
