import heapq
from Node import Node
from baseSearch import baseSearch

class Dijkstra(baseSearch):
    def __init__(self, iniX : int, iniY : int, destX : int, destY : int, typeCost : int):
        super().__init__(iniX,iniY,destX,destY,typeCost)
        # Dijkstra uses a min heap
        self.heap = []

    def doDijkstra(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return 
        
        # Nesse momento o nó com menor custo é a propria raiz com custo 0
        heapq.heappush(self.heap,self.root)
        
        while self.heap:
            # Removo o elemento com o menor custo
            self.currentNode = heapq.heappop(self.heap)
            if self.currentNode is not None and self.findNode(self.currentNode):
                self.visitedNodes.append(self.currentNode)

                if self.isObjective(self.currentNode):
                    print('Objective found!')
                    self.findPath(self.currentNode)
                    return

                
                neighbors = [
                    self.f1(self.currentNode),
                    self.f2(self.currentNode),
                    self.f3(self.currentNode),
                    self.f4(self.currentNode),
                ]

                for i, neighbor in enumerate(neighbors, start=1):
                    if neighbor is not None and self.findNode(neighbor):
                        # Atualizar o custo do vizinho
                        self.costFunc(neighbor, i)
                        # Adicionar à heap
                        heapq.heappush(self.heap, neighbor)
                        # Memorizar o nó gerado
                        self.genNodes.append(neighbor)
            else:
                continue
            
        print("Path not found")




