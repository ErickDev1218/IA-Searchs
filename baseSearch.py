from Node import Node
import math

class baseSearch:
    def __init__(self, iniX : int, iniY : int, destX : int, destY : int, typeCost : int = -1, heuristicCost : int = -1):
        print('Base search initialized')
        if self.limit(iniX,iniY):
            self.root = Node(iniX,iniY)
        else:
            self.root = None
        if self.limit(destX,destY):
            self.final = Node(destX,destY)
        else:
            self.final = None
        self.genNodes = [] # Vector to memorize all nodes has been created
        self.genNodes.append(self.root)
        self.visitedNodes = []
        self.currentNode = None
        self.typeCost = typeCost
        self.heuristicCost = heuristicCost
        self.costFunc = self.__choiceFunc(typeCost)

        self.heuristicFunc = self.__heuristicFunc(heuristicCost)
        
    def __heuristicFunc(self, choice : int):

        if choice == 1:
            return self.__h1
        elif choice == 2:
            return self.__h2
        else:
            return None
        
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
    #Distancia do nó atual até o nó alvo
    def __h2(self, node : Node, direction = -1):
        x1 = node.x
        y1 = node.y
        x2 = self.final.x
        y2 = self.final.y
        return (abs(x1 - x2) + abs(y1 - y2)) * 10

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
        
    def __c1(self, node : Node, direction = -1):
        node.cost += 10

    def __c2(self, node : Node, direction = -1):
        if direction == 3 or direction == 4:
            node.cost += 10
        elif direction == 1 or direction == 2:
            node.cost += 15
        else:
            return None
        
    def __c3(self, node : Node, direction = -1):
        if direction == 3 or direction == 4:
            node.cost += 10
        elif direction == 1 or direction == 2:
            # c3(t) = 10 + (|5 − t| mod 6)
            # onde t é o número passos (arestas) no caminho da raiz da árvore de busca até o estado que está sendo avaliado
            x = 10 + (abs(5 - node.deep) % 6)
            node.cost += x
        else:
            return None
        
    def __c4(self, node : Node, direction = -1):
        if direction == 3 or direction == 4:
            node.cost += 10
        elif direction == 1 or direction == 2:
            # c4(t) = 5 + (|10 − t| mod 11)
            # onde t é o número passos (arestas) no caminho da raiz da árvore de busca até o estado que está sendo avaliado
            x = 5 + (abs(10 - node.deep) % 11)
            node.cost += x
        else:
            return None

    def isObjective(self, node : Node) -> bool:
        if node.x == self.final.x and node.y == self.final.y:
            return True
        else:
            return False
        
    def limit(self, x : int, y: int):
        if (x > 30 or x < 0) or (y > 30 or y < 0):
            return False
        return True
    
        
    def findNode(self, node : Node) -> bool:
        for n in self.visitedNodes:
            if(n.x == node.x and n.y == node.y):
                return False
        return True
    
    def findPath(self, node : Node):
        current = node
        path = []
        while current.dad is not None:
            path.append(current)
            current = current.dad
            
        path.append(current)
        for i in range(len(path) - 1, -1, -1):
            if i == 0:
                print(f'({path[i].x}, {path[i].y})', end='')
            else:
                print(f'({path[i].x}, {path[i].y})', end=' -> ')

        print()
        print(f'Generated nodes: {len(self.genNodes)}')
        print(f'Level: {node.deep}')
        print(f'Path cost: {node.cost}')

    def f1(self, node : Node) -> Node:
       if node.x - 1 >= 0 :
           return Node(node.x - 1, node.y, node)
       else: 
           return None

    def f2(self, node : Node) -> Node:
        if node.x + 1 <= 30 :
           return Node(node.x + 1, node.y, node)
        else: 
           return None
    
    def f3(self, node : Node) -> Node:
        if node.y - 1 >= 0 :
           return Node(node.x, node.y - 1, node)
        else: 
            return None
        
    def f4(self, node : Node) -> Node:
        if node.y + 1 <= 30 :
           return Node(node.x, node.y + 1, node)
        else: 
           return None
    