from Node import Node
from baseSearch import baseSearch

class DFS(baseSearch): # Herança

    def __init__(self,iniX : int,iniY : int, destX : int, destY : int, typeCost : int):
        super().__init__(iniX,iniY,destX,destY,typeCost)
        # Busca em profundidade usa uma pilha
        self.stack = []

    
    
    def doDFS(self):

        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return 
        # Coloca a coordenada inicial na pilha
        self.stack.append(self.root)

        # Main loop
        while self.stack:
            # Remove a coordenada da pilha
            self.currentNode = self.stack.pop()

            # Expansao da coordenada
            if self.currentNode is not None:
                # Marca como visitada
                self.visitedNodes.append(self.currentNode)    

                # Checa se não é o objetivo
                if self.isObjective(self.currentNode):
                    print('Objective finded!')
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
                        # Coloca o nó na pilha e coloca o nó na lista dos filhos do pai
                        self.stack.append(neighbor)
                        self.currentNode.sons.append(neighbor)
            else:
                continue

        print("Path not found")


            


    