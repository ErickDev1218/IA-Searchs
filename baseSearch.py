from Node import Node
import math


# Esta é a classe base usada para todas as buscas. Notamos que todas a buscas usam praticamente as mesmas coisas
# salvo em sua especifidade, como estrutura de dados usada (heap, fila, pilha, etc ...), funcao de custo
# e heuristica.
class baseSearch:
    # Construtor base usado para as buscas.
    def __init__(self, iniX : int, iniY : int, destX : int, destY : int, typeCost : int = -1, heuristicCost : int = -1):
        if self.limit(iniX,iniY):
            self.root = Node(iniX,iniY)
        else:
            self.root = None
        if self.limit(destX,destY):
            self.final = Node(destX,destY)
        else:
            self.final = None
        self.genNodes = [] # Array usado para guardar os nós gerados.
        self.genNodes.append(self.root)
        self.visitedNodes = [] # Array usado para guardar os nós visitado.
        self.currentNode = None # Simula o ponteiro para o nó a ser expandido.
        self.typeCost = typeCost # Guarda o tipo de custo usado
        self.heuristicCost = heuristicCost # Guarda o tipo de heuristica usada 
        self.costFunc = self.__choiceFunc(typeCost) # Escolhe a funcao de custo que será aplicada.
        self.heuristicFunc = self.__heuristicFunc(heuristicCost) # Escolhe a funcao heuristica que será aplicada.
        self.Intermediates = [] # Array que guarda nós intermediários

    # Funcao que decide qual tipo de heuristica será usada
    def __heuristicFunc(self, choice : int):
        if choice == 1:
            return self.__h1
        elif choice == 2:
            return self.__h2
        else:
            return None
    # Definicao da heuristica 1
    def __h1(self, node : Node, direction = -1):
        x1 = node.x
        y1 = node.y
        x2 = self.final.x
        y2 = self.final.y
        return math.floor(
            math.sqrt(
                math.pow(abs(x1-x2),2) + math.pow(abs(y1-y2),2)
            ) * 10
        )
    # Definicao da heuristica 2
    def __h2(self, node : Node, direction = -1):
        x1 = node.x
        y1 = node.y
        x2 = self.final.x
        y2 = self.final.y
        return (abs(x1 - x2) + abs(y1 - y2)) * 10

    # Funcao que irá decidir qual funcao de custo será usada
    def __choiceFunc(self, choice : int):
        if choice == 1:
            return self.__c1
        elif choice == 2:
            return self.__c2
        elif choice == 3:
            return self.__c3
        elif choice == 4:
            return self.__c4
        else:
            return None
        
    # Definicao de C1
    def __c1(self, node : Node, direction = -1):
        node.cost += 10

    # Definicao de C2
    def __c2(self, node : Node, direction = -1):
        if direction == 3 or direction == 4:
            node.cost += 10
        elif direction == 1 or direction == 2:
            node.cost += 15
        else:
            return None
    
    # Definicao de C3
    def __c3(self, node : Node, direction = -1):
        if direction == 3 or direction == 4:
            node.cost += 10
        elif direction == 1 or direction == 2:
            # c3(t) = 10 + (|5 − t| mod 6)
            # onde t é o número passos (arestas) no caminho da raiz da árvore de busca
            # até o estado que está sendo avaliado
            x = 10 + (abs(5 - node.deep) % 6)
            node.cost += x
        else:
            return None
    
    # Definicao de C4
    def __c4(self, node : Node, direction = -1):
        if direction == 3 or direction == 4:
            node.cost += 10
        elif direction == 1 or direction == 2:
            # c4(t) = 5 + (|10 − t| mod 11)
            # onde t é o número passos (arestas) no caminho da raiz da árvore de busca
            # até o estado que está sendo avaliado
            x = 5 + (abs(10 - node.deep) % 11)
            node.cost += x
        else:
            return None

    # Funcao que verifica se o objetivo foi alcancado
    def isObjective(self, node : Node) -> bool:
        if node.x == self.final.x and node.y == self.final.y:
            return True
        else:
            return False
        
    def isIntermediate(self, node : Node) -> bool:
        for currentInt in self.Intermediates:
            if node.x == currentInt.x and node.y == currentInt.y:
                return True
        return False

    # Funcao que limita o espaco de busca (0,0) e (30,30)
    def limit(self, x : int, y: int):
        if (x > 30 or x < 0) or (y > 30 or y < 0):
            return False
        return True
    
    # Funcao que verifica se o nó já foi expandido
    def findNode(self, node : Node) -> bool:
        for n in self.visitedNodes:
            if(n.x == node.x and n.y == node.y):
                return False
        return True
    
    # Funcao que printa quando o objetivo é encontrado
    def findPath(self, node : Node):
        current = node
        path = []
        while current.dad is not None:
            path.append(current)
            current = current.dad
        path.append(current)
        # initialNode = f'Initial node: ({self.root.x},{self.root.y})'
        # finalNode = f'Objective node: ({self.final.x},{self.final.y})'
        print(f'Initial node: ({self.root.x},{self.root.y})')
        print(f'Objective node: ({self.final.x},{self.final.y})')
        print('Path found:')
        for i in range(len(path) - 1, -1, -1):
            if i == 0:
                print(f'({path[i].x}, {path[i].y})', end='')
            else:
                print(f'({path[i].x}, {path[i].y})', end=' -> ')
        print()
        print(f'Path cost: {node.cost}')
        print(f'Generated nodes: {len(self.genNodes)}')
        print(f'Visited nodes: {len(self.visitedNodes)}')

    # Funcao que expande o nó em f1(x)
    def f1(self, node : Node) -> Node:
       if node.x - 1 >= 0 :
           return Node(node.x - 1, node.y, node)
       else: 
           return None

    # Funcao que expande o nó em f2(x)
    def f2(self, node : Node) -> Node:
        if node.x + 1 <= 30 :
           return Node(node.x + 1, node.y, node)
        else: 
           return None
    
    # Funcao que expande o nó em f3(x)
    def f3(self, node : Node) -> Node:
        if node.y - 1 >= 0 :
           return Node(node.x, node.y - 1, node)
        else: 
            return None

    # Funcao que expande o nó em f4(x) 
    def f4(self, node : Node) -> Node:
        if node.y + 1 <= 30 :
           return Node(node.x, node.y + 1, node)
        else: 
           return None
    