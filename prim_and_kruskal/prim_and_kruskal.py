class Disjoint:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.arr = [-1 for elem in range(num_nodes)]

    def find_root(self, index):
        res = index
        while self.arr[res] >= 0:
            res = self.arr[res]
        return res

    def union(self, index1, index2):
        root1 = self.find_root(index1)
        root2 = self.find_root(index2)

        if root1 == root2:
            return False
        if self.arr[root1] <= self.arr[root2]:
            self.arr[root1] = self.arr[root1] + self.arr[root2]
            self.arr[root2] = root1
        else:
            self.arr[root2] = self.arr[root1] + self.arr[root2]
            self.arr[root1] = root2
        return True

class Edge:
    def __init__(self, node1, node2, weight):
        self.edge = (min(node1, node2), max(node1, node2))
        self.weight = weight

def parseInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    num_nodes = int(lines[0])
    edge_list = []
    for edge in lines[1:]:
        edge = [int(x) for x in edge.split()]
        edge = Edge(edge[0], edge[1], edge[2])
        edge_list.append(edge)
    return num_nodes, edge_list

def kruskal(num_nodes, edge_list):
    edge_list.sort(key=lambda x: x.weight)
    MST = []
    disjoint_set = Disjoint(num_nodes)

    for edge in edge_list:
        if disjoint_set.union(edge.edge[0], edge.edge[1]):
            MST.append(edge)
    
    return MST

def prim(num_nodes, edge_list, start_node):
    edge_list.sort(key=lambda x: x.weight)

    MST = []

    U = {start_node}
    V = {i for i in range(num_nodes)}
    while U != V:
        for i in edge_list:
            if (i.edge[0] not in U) and (i.edge[1] not in U):
                continue
            elif (i.edge[0] in U) and (i.edge[1] in U):
                continue
            else:
                MST.append(i)
                if i.edge[0] in U:
                    U.add(i.edge[1])
                else:
                    U.add(i.edge[0])
                break
    return MST

if __name__ == "__main__":
    num_nodes, edge_list = parseInput("input1.txt")
    MST = kruskal(num_nodes, edge_list)
    for i in MST:
        print(i.edge, i.weight)
    print("-----------------------------")
    MST = prim(num_nodes, edge_list, 1)
    for i in MST:
        print(i.edge, i.weight)