from baseSearch import baseSearch
import heapq

#Greedy Best-First Search
class GBFS(baseSearch):
    def __init__(self, iniX, iniY, destX, destY, typeCost, typeHeuristc):
        super().__init__(iniX, iniY, destX, destY, typeCost, typeHeuristc)
        self.queue = [] # Queue para percorrer em largura
        self.heap = []  #Heap de prioridade com os custo de cada node até o alvo
    
    def doGBFS(self):
        if self.root == None or self.final == None:
            print('Error: some limit has overflow.')
            return
        self.queue.append(self.root)
        
        while self.queue:
            """
            Tire o primeiro elemento da fila
                se o elemento for o buscado:
                    mostre o caminho
                se nao 
                gere n1, n2 ,n3 ,n4 e defina suas distancias até o targe
                para cada no gerado veja se ele nao eh nulo e coloque na fila de prioridade:
                    pegue o primeiro elemento da fila(menor distancia) e o coloque na fila
            
            
            """
            self.currentNode = self.queue.pop(0)
            if self.currentNode is not None:
                self.visitedNodes.append(self.currentNode)

                if self.isObjective(self.currentNode):
                    print('Objective found!')
                    self.findPath(self.currentNode)
                    return

                n1 = self.f1(self.currentNode)
                n2 = self.f2(self.currentNode)
                n3 = self.f3(self.currentNode)
                n4 = self.f4(self.currentNode)
                neighbors = [n1, n2, n3, n4]

                for i, neighbor in enumerate(neighbors, start=1):
                    if neighbor is not None and self.findCreateNode(neighbor):
                        self.genNodes.append(neighbor)
                    if neighbor is not None and self.findNode(neighbor):
                        #Não está privada
                        self.costFunc(neighbor,i) #Coloca o custo na função
                        neighbor.costToTarget = self.heuristicFunc(neighbor)
                        #heapq.heappush(self.heap,(neighbor, neighbor.cost_to_target))
                        heapq.heappush(self.heap,neighbor)
                        no = heapq.heappop(self.heap)
                        self.queue.append(no)
                        heapq.heapify(self.heap)
                        self.heap.clear()
                        #print(neighbor.cost_to_Target)
                        self.currentNode.sons.append(neighbor)
            else:
                continue