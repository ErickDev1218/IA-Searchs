from Node import Node
from baseSearch import baseSearch

class DFS(baseSearch): # Herança

    def __init__(self,iniX : int,iniY : int, destX : int, destY : int, typeCost : int):
        super().__init__(iniX,iniY,destX,destY,typeCost)
        # Deep search uses one stack
        self.stack = []

    
    
    def doDFS(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return 
        
        self.stack.append(self.root)

        # Main loop
        while self.stack:
            self.currentNode = self.stack.pop()
            if self.currentNode is not None:
                self.visitedNodes.append(self.currentNode)    

                if self.isObjective(self.currentNode):
                    print('Objective finded!')
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
                        self.stack.append(neighbor)
                        self.currentNode.sons.append(neighbor)
            else:
                continue




            


    