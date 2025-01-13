from DFS import DFS
from BFS import BFS
from AStar import AStar
from Node import Node
import heapq
from baseSearch import baseSearch
from Dijkstra import Dijkstra
from GBFS import GBFS

def main():
    d = Dijkstra(0,0,15,15,3)
    d.doDijkstra()
    print("===========")
    g = AStar(0,0,15,15,3,1)
    g.doAStar()
    # i = BFS(0,0,7,7)
    # i.doBFS()
    print("===========")
    h = GBFS(0,0,15,15,3,1)
    h.doGBFS()
    # (10, No.cost = 11)
    # (11, no.cost = 10)


main()