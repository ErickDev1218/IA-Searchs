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
    
    def Do(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return
        #Primeiro elemento da heap é o root
        self.add_to_queue(self.root)     
        while self.queue:
            # Remocao da tripla de (Distancia ate o no, ordem de criacao, nó)
            _,_, self.currentNode = self.pop_from_queue()

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
        print('Path not found')

    def DoInter(self, intermeds):
 
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return
        
        auxIni = self.root
        self.Intermediates = intermeds

        #Primeiro elemento da heap é o root
        self.add_to_queue(self.root)     

        flag = True
        while self.queue:
            # Remocao da tripla de (Distancia ate o no, ordem de criacao, nó)
            _,_, self.currentNode = self.pop_from_queue()

            # Expansao da coordenada
            if self.currentNode is not None and self.findNode(self.currentNode):

                # Marca como visitada caso seja diferente do objetivo
                
                self.visitedNodes.append(self.currentNode)

                # Checa se é o objetivo e já passou por um intermediário
                if self.isObjective(self.currentNode) and self.currentNode.passedThroughIntermediate:
                    self.root = auxIni
                    self.visitedNodes.append(self.currentNode)
                    self.visitedNodes += self.visitedAux
                    print('Objective found!')
                    self.findPath(self.currentNode)

                    string = 'Intermediate points available: '
                    for x in self.Intermediates:
                        string += f"({x.x},{x.y}), "
                    print(string)

                    print(f'Intermediate point used: ({self.Intermediate.x},{self.Intermediate.y})')

                    return
                
                # Checa se o nó atual é um intermediário, caso seja atualiza a flag do caminho
                if self.isIntermediate(self.currentNode) and flag:
                    self.currentNode.passedThroughIntermediate = True
                    self.root = self.currentNode
                    self.queue = []
                    self.add_to_queue(self.root)
                    self.visitedAux = self.visitedNodes
                    self.visitedNodes = []
                    self.Intermediate = self.currentNode
                    flag = False
                    # print(self.currentNode.passedThroughIntermediate)
                    

                # Gera as coordenadas vizinhas
                neighbors = [
                    self.f1(self.currentNode),
                    self.f2(self.currentNode),
                    self.f3(self.currentNode),
                    self.f4(self.currentNode)
                ]

                for i,neighbor in enumerate(neighbors,start=1):
                    # Verifica se o nó ja foi expandido
                    if neighbor is not None and self.findNode(neighbor):
                        # Coloca o nó na lista de nós gerados
                        self.genNodes.append(neighbor)
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

        print('Path not found')