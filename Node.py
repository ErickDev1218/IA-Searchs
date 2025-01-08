class Node:
    def __init__(self, xValue : int, yValue : int, dad : 'Node' = None):
        self.x = xValue
        self.y = yValue 
        self.dad = dad
        self.deep = 1 if dad is None else dad.deep + 1