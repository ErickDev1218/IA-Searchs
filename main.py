from DFS import DFS
from BFS import BFS
from AStar import AStar
from Dijkstra import Dijkstra
from GBFS import GBFS
import random
import sys

def exp0():
    iniX = random.randint(0,30)
    iniY = random.randint(0,30)
    finX = random.randint(0,30)
    finY = random.randint(0,30)
    randCost = random.randint(1,4)
    randHeur = random.randint(1,2)
    print(iniX,iniY,finX,finY)

    v = [
        ('DFS',DFS(iniX,iniY,finX,finY,randCost)),
        ('BFS',BFS(iniX,iniY,finX,finY,randCost)),
        ('Dijkstra',Dijkstra(iniX,iniY,finX,finY,randCost)),
        ('GBFS',GBFS(iniX,iniY,finX,finY,randCost,randHeur)),
        ('A*',AStar(iniX,iniY,finX,finY,randCost,randHeur)),
    ]
    with open("Experimento-0.txt", "w") as file:
        for name,x in v:
            sys.stdout = file  # Redireciona tudo que vai para stdout
            print(f'Used algorithm: {name}')
            x.Do()
            print('\n*** ---------------------- ***\n')
    
def exp1():

    with open("Experimento-1.txt", "w") as file:
        for _ in range(50):
            iniX = random.randint(0,30)
            iniY = random.randint(0,30)
            finX = random.randint(0,30)
            finY = random.randint(0,30)

            for typeCost in range(1,5):
                v = [
                    ('DFS',DFS(iniX,iniY,finX,finY,typeCost)),
                    ('BFS',BFS(iniX,iniY,finX,finY,typeCost)),
                    ('Dijkstra',Dijkstra(iniX,iniY,finX,finY,typeCost)),
                ]
                for name,x in v:
                    sys.stdout = file
                    print(f'\nInitial: ({iniX},{iniY}), final: ({finX},{finY}), cost function: c{typeCost}\n')
                    print(f'Used algorithm: {name}')
                    x.Do()
                    print('\n*** ---------------------- ***\n')
            

def exp2():
    with open("Experimento-2.txt", "w") as file:
        for _ in range(50):
            iniX = random.randint(0,30)
            iniY = random.randint(0,30)
            finX = random.randint(0,30)
            finY = random.randint(0,30)

            for typeCost in range(1,5): # Fn(x) -> n = [1,4]
                v = [
                    ('Dijkstra',Dijkstra(iniX,iniY,finX,finY,typeCost)),
                ]
                for name,x in v:
                    sys.stdout = file
                    print(f'\nInitial: ({iniX},{iniY}), final: ({finX},{finY}), cost function: c{typeCost}\n')
                    print(f'Used algorithm: {name}')
                    x.Do()
                    print('\n*** ---------------------- ***\n')
                    for i in range(1,3): # Hm(x) -> m = [1,2]
                        print(f'\nInitial: ({iniX},{iniY}), final: ({finX},{finY}), cost function: c{typeCost}, heuristic: h{i}\n')
                        print(f'Used algorithm: A*')
                        AStar(iniX,iniY,finX,finY,typeCost,i).Do()
                        print('\n*** ---------------------- ***\n')

def exp3():
    with open("Experimento-3.txt", "w") as file:
        for _ in range(50):
            iniX = random.randint(0,30)
            iniY = random.randint(0,30)
            finX = random.randint(0,30)
            finY = random.randint(0,30)

            for heuristc in range(1,3):
                for typeCost in range(1,5):
                    v = [
                        ('GBFS',GBFS(iniX,iniY,finX,finY,typeCost,heuristc)),
                        ('A*',AStar(iniX,iniY,finX,finY,typeCost,heuristc)),
                    ]
                    for name,x in v:
                        sys.stdout = file
                        print(f'\nInitial: ({iniX},{iniY}), final: ({finX},{finY}), cost function: c{typeCost}, heuristic: h{heuristc}\n')
                        print(f'Used algorithm: {name}')
                        x.Do()
                        print('\n*** ---------------------- ***\n')

def exp4():
    with open("Experimento-4.txt", "w") as file:
        for _ in range(20):
            iniX = random.randint(0,3)
            iniY = random.randint(0,3)
            finX = random.randint(0,3)
            finY = random.randint(0,3)

            for _ in range(10):
                for typeCost in range(1,5):
                    v = [
                        ('DFS',DFS(iniX,iniY,finX,finY,typeCost, True)),
                        ('BFS',BFS(iniX,iniY,finX,finY,typeCost, True)),
                    ]
                    for name,x in v:
                        sys.stdout = file
                        print(f'\nInitial: ({iniX},{iniY}), final: ({finX},{finY}), cost function: c{typeCost}, randomization: {True}\n')
                        print(f'Used algorithm: {name}')
                        x.Do()
                        print('\n*** ---------------------- ***\n')
def main():
    exp4()


main()