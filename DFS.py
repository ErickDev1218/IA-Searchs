from Node import Node
from baseSearch import baseSearch

class DFS(baseSearch): # Herança

    def __init__(self,x : int,y : int):
        self.root = Node(x,y)
        super().f1(self.root) # Chamada de método da classe pai

    