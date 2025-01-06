class Node:
    def __init__(self, xValue : int, yValue : int):
        self.x = xValue if xValue <= 30 else xValue % 30 
        self.y = yValue if yValue <= 30 else yValue % 30
        self.son = []
        
    def pushNode(self, node : 'Node'):
        self.son.append(node)