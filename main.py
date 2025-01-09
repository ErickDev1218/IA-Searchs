from DFS import DFS
from BFS import BFS
from Node import Node
import heapq
from baseSearch import baseSearch
from Dijkstra import Dijkstra
from GBFS import GBFS

def main():
    g = GBFS(0,0,1,1,1,1)
    g.doGBFS()

main()