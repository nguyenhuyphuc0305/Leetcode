'''
    Problem: Write implementation for dijkstra algorithm given Adjacency Matrix and start_point
             Write implementation for floyd algorithm given Adjacency Matrix
'''

import math

# Given input file, return Adjacency Matrix
# Input file format:
#   Line 1: The number of Nodes in the Graph
#   Lines 2-EOF: Every other line in the file contains an edge
#       First Value is the FROM node
#       Second Value is the TO node
#       Third Value is the weight of the edge
def parseInput(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    
    numNodes = int(lines[0])
    adjacencyList = lines[1:]
    adjacencyMatrix = [[math.inf for elem in range(numNodes)] for row in range(numNodes)]
    
    for node in range(numNodes):
        adjacencyMatrix[node][node] = 0

    for edge in adjacencyList:
        edge = edge.split()
        adjacencyMatrix[int(edge[0])][int(edge[1])] = float(edge[2])

    return adjacencyMatrix 

# Node class for the heap array, containing attributes about node index and weight to get to that node from starting point
class Node:
    def __init__(self, nodeID, val):
        self.nodeID = nodeID
        self.val = val

    def __str__(self):
        return "Node index: " + str(self.nodeID) + ", Value: " + str(self.val)

# Heap class for the heap array. Each element is a Node. Delete with downheap wasn't implemented as I don't need it
class NodeHeap:
    def __init__(self):
        self.data = []
        self.res = ""

    def __str__(self):
        for i in self.data:
            self.res = self.res + str(i) + "\n"
        return self.res[:-1]
    
    def is_empty(self):
        return (self.data == [])

    def make_null(self):
        self.data = []

    def parent(self, index):
        return math.floor((index - 1) / 2)

    def left(self, index):
        return (2 * index + 1)

    def right(self, index):
	    return (2 * index + 2)

    def swap(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def insert(self, x: Node):
        self.data.append(x)
        self.upheap(len(self.data) - 1)

    def upheap(self, index):
        if self.parent(index) < 0:
            return
        if self.data[self.parent(index)].val < self.data[index].val:
            return
        self.swap(index, self.parent(index))
        self.upheap(self.parent(index))

    def delete_min(self):
        self.swap(0, len(self.data) - 1)
        self.data.pop()

    def find_node_by_ID(self, nodeID):
        for i in self.data:
            if i.nodeID == nodeID:
                return i
        return None

    def fix_heap(self):
        temp = self.data[:]
        self.make_null()
        for i in temp:
            self.insert(i)

# dijkstra implementation based on Adjacency Matrix, return weight list from starting point
def dijkstra(adjacencyMatrix, start_node: int):
    numNodes = len(adjacencyMatrix)

    heap = NodeHeap()
    distance_list = [math.inf] * numNodes
    distance_list[start_node] = 0

    for i in range(numNodes):
        if i == start_node:
            new_node = Node(i, 0)
        else:
            new_node = Node(i, math.inf)

        heap.insert(new_node)
    
    while not heap.is_empty():
        min_node_cost = distance_list[heap.data[0].nodeID]
        min_list = adjacencyMatrix[heap.data[0].nodeID]
        for i in range(len(min_list)):
            found_node = heap.find_node_by_ID(i)
            if (found_node != None) and (min_node_cost + min_list[i] < heap.find_node_by_ID(i).val):
                heap.find_node_by_ID(i).val = min_node_cost + min_list[i]
                distance_list[i] = min_node_cost + min_list[i]
        heap.delete_min()
        heap.fix_heap()     

    return distance_list

# floyd implemenation from Adjacency Matrix, return a new 2-d array contains all the updated weights 
# Runtime: O(n^3)
def floyd(adjacencyMatrix):
    numNodes = len(adjacencyMatrix)
    # With each element in 2-d array Adjacency Matrix (each element is the weight between 2 node FROM i and TO j), we find a node k in between that:
    #       (weight of i -> k + weight of k -> j) < (weight of i -> j) and updated the better path to Adjacency Matrix 
    for k in range(numNodes):
        for i in range(numNodes):
            for j in range(numNodes):
                if adjacencyMatrix[i][j] > adjacencyMatrix[i][k] + adjacencyMatrix[k][j]:
                    adjacencyMatrix[i][j] = adjacencyMatrix[i][k] + adjacencyMatrix[k][j]
    
    return adjacencyMatrix

if __name__ == "__main__":
    adjacencyMatrix = parseInput("input1.txt")
    print(dijkstra(adjacencyMatrix,0))
    print(floyd(adjacencyMatrix))

