from baseSearch import baseSearch
import heapq

# Greedy Best-First Search
class GBFS(baseSearch):
    def __init__(self, iniX, iniY, destX, destY, typeCost, typeHeuristc):
        super().__init__(iniX, iniY, destX, destY, typeCost, typeHeuristc)
        self.heap = []  # Heap de prioridade com os custos de cada nó até o alvo            
    
    def doGBFS(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return
        heapq.heappush(self.heap, (self.heuristicFunc(self.root), self.root))  # Começa com o nó inicial        
        while self.heap:
            #Tupla de (Distancia ate o no, No)
            _, currentNode = heapq.heappop(self.heap)
            if currentNode is not None:
                self.visitedNodes.append(currentNode)

                if self.isObjective(currentNode):
                    print('Objective found!')
                    self.findPath(currentNode)
                    return

                n1 = self.f1(currentNode)
                n2 = self.f2(currentNode)
                n3 = self.f3(currentNode)
                n4 = self.f4(currentNode)
                neighbors = [n1, n2, n3, n4]

                for neighbor in neighbors:
                    if neighbor is not None and self.findCreateNode(neighbor):
                        self.genNodes.append(neighbor)
                    if neighbor is not None and self.findNode(neighbor):
                        # Calcular a distância até o alvo
                        neighbor.cost_to_target = self.heuristicFunc(neighbor)
                        # Tupla que contém (Distância até o target, o Nó)
                        heapq.heappush(self.heap, (neighbor.cost_to_target, neighbor))
                        currentNode.sons.append(neighbor)
            else:
                continue
