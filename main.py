from DFS import DFS
from BFS import BFS
from AStar import AStar
from Dijkstra import Dijkstra
from GBFS import GBFS
import random
import sys
import pandas as pd
from io import StringIO
import re

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
    
def exp1_txt():

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
            initial_match = re.search(r"Initial: \((\d+,\d+)\)", block)
            final_match = re.search(r"final: \((\d+,\d+)\)", block)
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
            
            # Valores opcionais
            heuristic = heuristic_match.group(1) if heuristic_match else None
            randomization = randomization_match.group(1) if randomization_match else None
            
            # Adicionar ao resultado
            results.append([
                initial, final, cost_function, algorithm, objective_found,
                path_cost, generated_nodes, visited_nodes, heuristic, randomization
            ])
    
    # Colunas do DataFrame
    columns = [
        "Initial", "Final", "Cost Function", "Algorithm", "Objective Found",
        "Path Cost", "Generated Nodes", "Visited Nodes", "Heuristic", "Randomization"
    ]
    
    # Converter para DataFrame
    df = pd.DataFrame(results, columns=columns)

    # Checa se utiliza Heuristica e Randomization
    if df["Heuristic"].isna().all():
        df = df.drop(columns=["Heuristic"])
    if df["Randomization"].isna().all():
        df = df.drop(columns=["Randomization"])

    return df




def exp2_txt():
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

def exp3_txt():
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

def exp4_txt():
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
    # df_results = exp1_csv()
    # df_results
    # df_results.to_csv("Experimento-1.csv", index=False)
    # Caminho para o arquivo .txt
    # exp1_txt()
    # exp2_txt()


    file_path = "Experimento-4.txt"

    # Processar o arquivo e criar o DataFrame
    df_results = process_txt_to_dataframe(file_path)

    # Exibir o DataFrame
    print(df_results)

    # Salvar como CSV (opcional)
    df_results.to_csv("Experimento-4.csv", index=False)


main()