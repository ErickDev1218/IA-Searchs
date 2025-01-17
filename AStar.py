from baseSearch import baseSearch
from Node import Node
import itertools

# realObj = 0

# A* Search
class AStar(baseSearch):
    def __init__(self, iniX : int, iniY: int, destX: int, destY: int, typeCost: int, typeHeuristic: int):
        super().__init__(iniX, iniY, destX, destY, typeCost, typeHeuristic)
        self.queue = []  # Lista que substitui a heap
        self.counter = itertools.count()  # Para manter a ordem de geração dos nós          
    
    # Funcoes adicionais para corrigir a falha da heap que estava comparando pela heuristica e, caso empate,
    # estava comparando pelo custo. Agora, caso a heuristica empate, o próximo critério é a ordem de criação.
    def add_to_queue(self, node):
        # Adiciona o nó à lista com os critérios desejados
        creation_order = next(self.counter)
        self.queue.append((node.costToTarget, creation_order, node))
        # Ordena a lista por heurística e depois pela ordem de geração
        self.queue.sort(key=lambda x: (x[0], x[1]))

    def pop_from_queue(self):
        # Remove e retorna o próximo nó
        return self.queue.pop(0) if self.queue else None
    
    def Do(self, intermeds: Node = []):
    
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return
        # Atualiza o vetor de pontos de interesse
        if intermeds: 
            self.Intermediates = intermeds
            self.final.passedThroughIntermediate = True
        

        #Primeiro elemento da heap é o root
        self.add_to_queue(self.root)     

        while self.queue:
            # Remocao da tripla de (Distancia ate o no, ordem de criacao, nó)
            _,_, self.currentNode = self.pop_from_queue()

            # Expansao da coordenada
            if self.currentNode is not None and self.findNode(self.currentNode):
                # Marca como visitada
                self.visitedNodes.append(self.currentNode)
            
                # Caso seja passado uma lista de pontos de interesse, checa se e um ponto de interesse e atualiza o valor de passedThroughIntermediate
                if self.Intermediates:
                    if self.isIntermediate(self.currentNode):
                        self.currentNode.passedThroughIntermediate = True
                        self.Intermediate = self.currentNode

                # Checa se não é o objetivo
                if self.isObjective(self.currentNode):
                    print('Objective found!')
                    self.findPath(self.currentNode)
                    if intermeds:
                        string = 'Intermediate points available: '
                        for x in self.Intermediates:
                            string += f"({x.x},{x.y}), "
                        print(string)

                        print(f'Intermediate point used: ({self.Intermediate.x},{self.Intermediate.y})')
                        return
                

                # Gera as coordenadas vizinhas
                neighbors = [
                    self.f1(self.currentNode),
                    self.f2(self.currentNode),
                    self.f3(self.currentNode),
                    self.f4(self.currentNode)
                ]

                for i,neighbor in enumerate(neighbors,start=1):
                    if neighbor is not None:
                        # Marca o nó como nó gerado
                        self.genNodes.append(neighbor)
                    # Verifica se o nó já foi expandido
                    if neighbor is not None and self.findNode(neighbor):
                        # Atualiza o custo do caminho de acordo com a funcao de custo 
                        self.costFunc(neighbor, i)
                        # Calcula o f(n) = g(n) + h(n)
                        neighbor.costToTarget = self.heuristicFunc(neighbor) + neighbor.cost
                        # Adiciona a fila
                        self.add_to_queue(neighbor)
                        # Coloca o nó na lista dos filhos do pai
                        self.currentNode.sons.append(neighbor)
            else:
                continue