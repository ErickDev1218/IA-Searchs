from DFS import DFS
from BFS import BFS
from GBFS import GBFS
from AStar import AStar
from Dijkstra import Dijkstra
from Node import Node
import random
import sys
import pandas as pd
import re


def process_txt_to_dataframe(file_path):
    # Abrir o arquivo e ler o conteúdo
    with open(file_path, "r") as file:
        data = file.read()
    
    # Dividir o conteúdo em blocos, considerando o separador "*** ---------------------- ***"
    blocks = data.split("*** ---------------------- ***")
    
    # Lista para armazenar os resultados processados
    results = []

    # Processar cada bloco
    for block in blocks:
        if block.strip():  # Ignorar blocos vazios
            # Extrair informações obrigatórias
            initial_match = re.search(r"Initial node: \((\d+,\d+)\)", block)
            final_match = re.search(r"Objective node: \((\d+,\d+)\)", block)
            initial = f"({initial_match.group(1)})"
            final = f"({final_match.group(1)})"
            cost_function = re.search(r"cost function: (c\d+)", block).group(1)
            algorithm = re.search(r"Used algorithm: (\w+)", block).group(1)
            objective_found = "Objective found!" in block
            path_cost = re.search(r"Path cost: (\d+)", block).group(1)
            generated_nodes = re.search(r"Generated nodes: (\d+)", block).group(1)
            visited_nodes = re.search(r"Visited nodes: (\d+)", block).group(1)
            
            # Verificar campos opcionais
            heuristic_match = re.search(r"heuristic: (\w+)", block)
            randomization_match = re.search(r"randomization: (\w+)", block)
            intermediate_match = re.search(r"Intermediate point used: \((\d+,\d+)\)", block)
            
            # Valores opcionais
            heuristic = heuristic_match.group(1) if heuristic_match else None
            randomization = randomization_match.group(1) if randomization_match else None
            intermediate = f"({intermediate_match.group(1)})" if intermediate_match else None
            
            # Adicionar ao resultado
            results.append([
                initial, final, cost_function, algorithm, objective_found,
                path_cost, generated_nodes, visited_nodes, heuristic, randomization, intermediate
            ])
    
    # Colunas do DataFrame
    columns = [
        "Initial", "Final", "Cost Function", "Algorithm", "Objective Found",
        "Path Cost", "Generated Nodes", "Visited Nodes", "Heuristic", "Randomization", "Intermediate"
    ]
    
    # Converter para DataFrame
    df = pd.DataFrame(results, columns=columns)

    # Checa se utiliza Heuristica e Randomization
    if df["Heuristic"].isna().all():
        df = df.drop(columns=["Heuristic"])
    if df["Randomization"].isna().all():
        df = df.drop(columns=["Randomization"])
    if df["Intermediate"].isna().all():
        df = df.drop(columns=["Intermediate"])

    return df

# Implementado apenas para fim de teste (como sugerido no documento).
def exp0():
    original_stdout = sys.stdout
    iniX = random.randint(0,30)
    iniY = random.randint(0,30)
    finX = random.randint(0,30)
    finY = random.randint(0,30)
    randCost = random.randint(1,4)
    randHeur = random.randint(1,2)

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
    sys.stdout = original_stdout
    
def exp1():
    original_stdout = sys.stdout
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
    sys.stdout = original_stdout

           
def exp2():
    original_stdout = sys.stdout
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
    sys.stdout = original_stdout

def exp3():
    original_stdout = sys.stdout
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
    sys.stdout = original_stdout

def exp4():
    original_stdout = sys.stdout
    with open("Experimento-4.txt", "w") as file:
        for _ in range(20):
            iniX = random.randint(0,30)
            iniY = random.randint(0,30)
            finX = random.randint(0,30)
            finY = random.randint(0,30)

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
    sys.stdout = original_stdout

def exp5():
    original_stdout = sys.stdout
    with open("Experimento-5.txt", "w") as file:
        for _ in range(25):
            iniX = random.randint(0,30)
            iniY = random.randint(0,30)
            finX = random.randint(0,30)
            finY = random.randint(0,30)
            inter1X = random.randint(0,30)
            inter1Y = random.randint(0,30)
            inter2X = random.randint(0,30)
            inter2Y = random.randint(0,30)
            inter3X = random.randint(0,30)
            inter3Y = random.randint(0,30)
            inter4X = random.randint(0,30)
            inter4Y = random.randint(0,30)

            intermeds = [Node(inter1X, inter1Y), Node(inter2X, inter2Y), Node(inter3X, inter3Y), Node(inter4X, inter4Y)]
 
            for typeCost in range(1,5):
                for typeHeuristic in range(1,3):
                    v = AStar(iniX,iniY,finX,finY,typeCost,typeHeuristic)
                    sys.stdout = file
                    print(f'Used algorithm: A*')
                    print(f'\nInitial: ({iniX},{iniY}), final: ({finX},{finY}), cost function: c{typeCost}, heuristic: h{typeHeuristic}\n')
                    v.Do(intermeds)
                    print('\n*** ---------------------- ***\n')
    sys.stdout = original_stdout


def makeExp():
    # Gera os arquivos .txt
    exps = [
        (1, exp1),
        (2, exp2),
        (3, exp3),
        (4, exp4),
        (5, exp5),
    ]
    # Gera os arquivos .txt
    for _,exp in exps:
        exp()
    
    # Gera os arquivos .csv
    for i,_ in exps:
        file_path = f'Experimento-{i}.txt'
        # Processar o arquivo e criar o DataFrame
        df_results = process_txt_to_dataframe(file_path)
        # Salvar como CSV
        df_results.to_csv(f"Experimento-{i}.csv", index=False)

    # Após essa função, o resto se dá no arquivo .ipynb
