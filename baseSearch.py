from Node import Node


class baseSearch:
    def __init__(self, iniX : int, iniY : int, destX : int, destY : int):
        print('Base search initialized')
        self.root = Node(iniX,iniY)
        self.final = Node(destX,destY)
        self.genNodes = [] # Vector to memorize all nodes has been created
        self.genNodes.append(self.root)
        self.visitedNodes = []
        self.currentNode = None

    def isObjective(self, node : Node) -> bool:
        if node.x == self.final.x and node.y == self.final.y:
            return True
        else:
            return False
        
    def findNode(self, node : Node) -> bool:
        for n in self.genNodes:
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
            print(f'({path[i].x}, {path[i].y})')
        print(f'Quantidade de Nodes gerados: {len(self.genNodes)} ')

    def f1(self, node : Node) -> Node:
       new_x = node.x - 1 if node.x >= 1 else 0
       return Node(new_x, node.y, node)

    def f2(self, node : Node) -> Node:
        new_x = node.x + 1 if node.x < 30 else 0
        return Node(new_x, node.y, node)    
    
    def f3(self, node : Node) -> Node:
        new_y = node.y - 1 if node.y >= 1 else 0
        return Node(node.x, new_y, node)

    def f4(self, node : Node) -> Node:
        new_y = node.y + 1 if node.y < 30 else 0
        return Node(node.x, new_y, node)