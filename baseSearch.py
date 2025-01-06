from Node import Node

class baseSearch:
    def __init__(self):
        print('Base search initialized')

    def f1(self, node : Node):
        node.x -= 1 if node.x >= 1 else 0

    def f2(self, node : Node):
        node.x += 1 if node.x < 30 else 0
    
    def f3(self, node : Node):
        node.y -= 1 if node.y >= 1 else 0

    def f4(self, node : Node):
        node.y += 1 if node.y < 30 else 0