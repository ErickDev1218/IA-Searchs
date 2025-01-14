from Node import Node
from baseSearch import baseSearch
import random

class BFS(baseSearch):  # Herança

    def __init__(self, iniX: int, iniY: int, destX: int, destY: int, typeCost : int, random : bool = False):
        super().__init__(iniX, iniY, destX, destY, typeCost)
        self.random = random
        # Busca em largura usa uma fila
        self.queue = []



    def Do(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return 
        # Coloca a coordenada inicial na fila
        self.queue.append(self.root)
        
        # Main loop
        while self.queue:
            # Remove a coordenada da fila
            self.currentNode = self.queue.pop(0)

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
                    (1,self.f1(self.currentNode)),
                    (2,self.f2(self.currentNode)),
                    (3,self.f3(self.currentNode)),
                    (4,self.f4(self.currentNode))
                ]

                if self.random:
                    random.shuffle(neighbors)

                for i,neighbor in neighbors:
                    if neighbor is not None:
                        # Marca o nó como nó gerado
                        self.genNodes.append(neighbor)
                    # Verifica se o nó já foi expandido
                    if neighbor is not None and self.findNode(neighbor):
                        # Atualiza o custo
                        self.costFunc(neighbor,i)
                        # Coloca o nó na fila e coloca o nó na lista dos filhos do pai
                        self.queue.append(neighbor)  
                        self.currentNode.sons.append(neighbor)
            else:
                continue
            
        print("Path not found")