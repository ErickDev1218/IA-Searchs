import heapq
from Node import Node
from baseSearch import baseSearch

class Dijkstra(baseSearch):
    def __init__(self, iniX : int, iniY : int, destX : int, destY : int, typeCost : int):
        super().__init__(iniX,iniY,destX,destY,typeCost)
        # Dijkstra usa uma heap minima
        self.heap = []

    def Do(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return 
        
        # Coloca a coordenada inicial na heap
        heapq.heappush(self.heap,self.root)
        
        # Main loop
        while self.heap:
            # Remove a coordenada da heap
            self.currentNode = heapq.heappop(self.heap)

            # Expansao da coordenada
            if self.currentNode is not None and self.findNode(self.currentNode):
                # Marca como visitada
                self.visitedNodes.append(self.currentNode)

                # Checa se não é o objetivo
                if self.isObjective(self.currentNode):
                    print('Objective found!')
                    self.findPath(self.currentNode)
                    return

                # Gera as coordenadas vizinhas
                neighbors = [
                    self.f1(self.currentNode),
                    self.f2(self.currentNode),
                    self.f3(self.currentNode),
                    self.f4(self.currentNode),
                ]

                for i, neighbor in enumerate(neighbors, start=1):
                    # Verifica se o nó já foi expandido
                    if neighbor is not None and self.findNode(neighbor):
                        # Atualizar o custo da coordenada vizinha
                        self.costFunc(neighbor, i)
                        # Adiciona à heap
                        heapq.heappush(self.heap, neighbor)
                        # Marca o nó como gerado e coloca o nó na lista dos filhos do pai
                        self.genNodes.append(neighbor)
                        self.currentNode.sons.append(neighbor)
            else:
                continue
            
        print("Path not found")




