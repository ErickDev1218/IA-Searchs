from DFS import DFS
from BFS import BFS
from Node import Node

def main():
   d = DFS(0,0,2,2,1)
   n = Node(1,2)
   d.costFunc(n)
   print(n.cost)

main()