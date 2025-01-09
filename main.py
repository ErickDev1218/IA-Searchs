from DFS import DFS
from BFS import BFS
from Node import Node
import heapq
from baseSearch import baseSearch
from Dijkstra import Dijkstra

def main():
    d = Dijkstra(0,0,3,8,1)
    d.doDijkstra()


main()