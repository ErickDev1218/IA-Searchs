from Node import Node


class baseSearch:
    def __init__(self, iniX : int, iniY : int, destX : int, destY : int):
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
            if i == 0:  # Último elemento
                print(f'({path[i].x}, {path[i].y})', end='')
            else:
                print(f'({path[i].x}, {path[i].y})', end=' -> ')

        print()  # Adiciona uma nova linha após o caminho
        print(f'Generated nodes: {len(self.genNodes)}')
        print(f'Level: {node.deep}')

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
        