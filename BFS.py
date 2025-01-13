from Node import Node
from baseSearch import baseSearch

class BFS(baseSearch):  # Herança

    def __init__(self, iniX: int, iniY: int, destX: int, destY: int):
        super().__init__(iniX, iniY, destX, destY)
        # Busca em largura usa uma fila
        self.queue = []



    def doBFS(self):
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
            if self.currentNode is not None:
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
                    self.f4(self.currentNode)
                ]

                for neighbor in neighbors:
                    if neighbor is not None:
                        # Marca o nó como nó gerado
                        self.genNodes.append(neighbor)
                    # Verifica se o nó já foi expandido
                    if neighbor is not None and self.findNode(neighbor):
                        # Coloca o nó na fila e coloca o nó na lista dos filhos do pai
                        self.queue.append(neighbor)  
                        self.currentNode.sons.append(neighbor)
            else:
                continue
            
        print("Path not found")