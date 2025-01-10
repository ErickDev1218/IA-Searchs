from DFS import DFS
from BFS import BFS
from Node import Node
import heapq
from baseSearch import baseSearch
from Dijkstra import Dijkstra
from GBFS import GBFS

def main():
    # d = Dijkstra(0,0,3,8,1)
    # d.doDijkstra()
    g = GBFS(0,0,2,2,3,1)
    g.doGBFS()
    # (10, No.cost = 11)
    # (11, no.cost = 10)


main()