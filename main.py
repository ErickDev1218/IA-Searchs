from DFS import DFS
from Node import Node

def main():
    n1 = Node(30,30)
    n2 = Node(25,25,n1)
    print(n1.dad)
    print(n2.dad.x)


main()