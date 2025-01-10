from baseSearch import baseSearch
import itertools

# Greedy Best-First Search
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
    
    def doAStar(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return
        #Primeiro elemento da heap é o root
        self.add_to_queue(self.root)     
        while self.queue:
            #Tupla de (Distancia ate o no, No)
            _,_, self.currentNode = self.pop_from_queue()
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

                for i,neighbor in enumerate(neighbors,start=1):
                    if neighbor is not None:
                        self.genNodes.append(neighbor)
                    if neighbor is not None and self.findNode(neighbor):
                        # Atualiza o custo do caminho de acordo com a costFunc
                        self.costFunc(neighbor, i)
                        # Calcular o f(n) = g(n) + h(n)
                        neighbor.costToTarget = self.heuristicFunc(neighbor) + neighbor.cost
                        self.add_to_queue(neighbor)
                        self.currentNode.sons.append(neighbor)
            else:
                continue
        print('Path not found')