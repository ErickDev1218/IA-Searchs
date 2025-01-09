class Node:
    def __init__(self, xValue : int, yValue : int, dad : 'Node' = None):
        self.x = xValue
        self.y = yValue 
        self.dad = dad
        self.deep = 1 if dad is None else dad.deep + 1
        self.cost = 0 if dad is None else dad.cost
        self.sons = []
        self.costToTarget = 0

    #Sobrecarga do operador < para usar na heap
    def __lt__(self, node : 'Node'):
        return self.cost < node.cost