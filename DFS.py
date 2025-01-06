from Node import Node
from baseSearch import baseSearch

class DFS(baseSearch): # Herança

    def __init__(self,x : int,y : int):
        super().__init__
        self.root = Node(x,y)
        self.f1(self.root) # Chamada de método da classe pai

    