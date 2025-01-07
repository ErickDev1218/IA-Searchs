from Node import Node
from baseSearch import baseSearch

class BFS(baseSearch):  # Herança

    def __init__(self, iniX: int, iniY: int, destX: int, destY: int):
        super().__init__(iniX, iniY, destX, destY)
        # Breadth-first search uses a queue 
        self.queue = []

    def doBFS(self):
        if self.isObjective(self.root):
            print('Objective found!')
            self.findPath(self.root)
            return
        
        self.queue.append(self.root)
        
        while self.queue:
            self.currentNode = self.queue.pop(0)
            self.visitedNodes.append(self.currentNode)

            # Verifica se o nó atual é o objetivo
            if self.isObjective(self.currentNode):
                print('Objective found!')
                print(self.currentNode.x, self.currentNode.y)
                self.findPath(self.currentNode)
                return

            # Gera os vizinhos (nós adjacentes)
            n1 = self.f1(self.currentNode)
            n2 = self.f2(self.currentNode)
            n3 = self.f3(self.currentNode)
            n4 = self.f4(self.currentNode)
            neighbors = [n1, n2, n3, n4]

            for neighbor in neighbors:
                if self.findNode(neighbor):
                    self.queue.append(neighbor)  
                    self.genNodes.append(neighbor)  
