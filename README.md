# IA-Searchs

# Documentação de Algoritmos de Busca

## Atenção!
É **muito importante** que a função `makeExp()` **não seja chamada novamente**, pois, caso isso aconteça, **todos os parâmetros utilizados na nossa análise serão alterados**. Isso pode comprometer a fidelidade da análise em relação ao novo experimento.

No arquivo `main.py`, deixaremos **instâncias comentadas predefinidas** de todos os algoritmos utilizados. Para realizar testes individuais, basta **remover o comentário** e ajustar os parâmetros.

### Parâmetros para Testes
Segue a descrição dos parâmetros necessários para realizar testes por conta própria:

---

## Classe Node
Esta classe deve ter os seguintes parâmetros:

- **x**, **y**: Um par de números inteiros que corresponde à coordenada do nó.
  - **Intervalo válido**: 0 a 30 para cada coordenada.

**Exemplo**:
```python
Node(3, 2)  # Um nó com coordenadas x = 3 e y = 2.
```

## Busca em profundidade (DFS):
Esta classe deve ter os seguintes parâmetros respectivamente:
- **X inicial,**
- **Y inicial,**
- **X final,**
- **Y final,**
  - número inteiro de 1 a 4 (representa a função de custo),
- **True**
  - (este parâmetro é opcional e só deve ser passado se você desejar utilizar randomização de vizinhança).

Exemplo: 
```python
DFS(0,0,1,1,3) #(0,0) -> (1,1) utilizando c3 e sem randomização de vizinhança.
```


## Busca em largura (BFS):
Esta classe deve ter os seguintes parâmetros respectivamente: X inicial, Y inicial, X final, Y final, número inteiro de 1 a 4 (representa a função de custo), True (este parâmetro é opcional e só deve ser passado se você desejar utilizar randomização de vizinhança).
Exemplo:
```python
BFS(0,0,1,1,3) # (0,0) -> (1,1) utilizando c3 e sem randomização de vizinhança.
```

## Custo uniforme (Dijkstra):
Esta classe deve ter os seguintes parâmetros respectivamente: X inicial, Y inicial, X final, Y final, número inteiro de 1 a 4 (representa a função de custo).
Exemplo: 
```python
Dijkstra(0,0,1,1,3) # (0,0) -> (1,1) utilizando c3.
```

## Busca gulosa (GBFS):
Esta classe deve ter os seguintes parâmetros respectivamente: X inicial, Y inicial, X final, Y final, número inteiro de 1 a 4 (representa a função de custo), número inteiro de 1 a 2 (representa a função heurística).
Exemplo:
```python
GBFS(0,0,1,1,3,1) # (0,0) -> (1,1) utilizando c3 e h1.
```

## A* (AStar):
Esta classe deve ter os seguintes parâmetros respectivamente: X inicial, Y inicial, X final, Y final, número inteiro de 1 a 4 (representa a função de custo), número inteiro de 1 a 2 (representa a função heurística).
Exemplo: 
```python
AStar(0,0,1,1,3,1) # (0,0) -> (1,1) utilizando c3 e h1.
```

## Considerações adicionais
Todas as classes supracitadas (com exceção da classe Node) implementam um método chamado “Do” que inicia a busca e nos traz os resultados.

Exemplo:
```python
AStar(0,0,1,1,3,1).Do()
```
**P.S:** Ao utilizar o método “Do” da classe AStar, é opcional passar uma lista de Nodes, para realizar a busca implementada na experimentação 5: Caminho Mínimo Com Uma Parada A Mais.

Exemplo: 
```python
intermeds = [Node(2,3), Node(1,3), Node(1,4)]
AStar(0,0,1,1,3,1).Do(intermeds)
```