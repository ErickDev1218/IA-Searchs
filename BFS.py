from Node import Node
from baseSearch import baseSearch

class BFS(baseSearch):  # Herança

    def __init__(self, iniX: int, iniY: int, destX: int, destY: int):
        super().__init__(iniX, iniY, destX, destY)
        # Breadth-first search uses a queue 
        self.queue = []



    def doBFS(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return 
        
        self.queue.append(self.root)
        
        # Main loop
        while self.queue:
            self.currentNode = self.queue.pop(0)
            if self.currentNode is not None:
                self.visitedNodes.append(self.currentNode)

                if self.isObjective(self.currentNode):
                    print('Objective found!')
                    self.findPath(self.currentNode)
                    return

                n1 = self.f1(self.currentNode)
                n2 = self.f2(self.currentNode)
                n3 = self.f3(self.currentNode)
                n4 = self.f4(self.currentNode)
                neighbors = [n1, n2, n3, n4]

                for neighbor in neighbors:
                    if neighbor is not None:
                        self.genNodes.append(neighbor)
                    if neighbor is not None and self.findNode(neighbor):
                        self.queue.append(neighbor)  
                        self.currentNode.sons.append(neighbor)
            else:
                continue
