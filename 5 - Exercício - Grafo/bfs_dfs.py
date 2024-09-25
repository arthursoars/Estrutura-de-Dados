from collections import deque  # Importa deque, uma estrutura de dados de fila otimizada da biblioteca collections

def bfs(grafo, start, end):
    # Inicializa uma lista para marcar quais vértices já foram visitados
    visitados = [False] * grafo.vertices
    # Cria uma fila (deque) com o vértice inicial 'start'
    fila = deque([start])
    # Inicializa uma lista para armazenar o "pai" de cada vértice, usado para reconstruir o caminho
    pais = [-1] * grafo.vertices

    # Marca o vértice inicial como visitado
    visitados[start] = True

    # Enquanto houver elementos na fila, continua o processo
    while fila:
        # Remove o próximo vértice da fila para processar
        vertice = fila.popleft()

        # Se o vértice atual for o vértice de destino, imprime o caminho
        if vertice == end:
            imprimir_caminho(pais, start, end)
            return
        
        # Itera sobre os vizinhos do vértice atual
        for vizinho in grafo.lista_adjacencia[vertice]:
            # Se o vizinho ainda não foi visitado, marca como visitado, coloca na fila e atualiza o "pai"
            if not visitados[vizinho]:
                fila.append(vizinho)  # Adiciona o vizinho à fila
                visitados[vizinho] = True  # Marca o vizinho como visitado
                pais[vizinho] = vertice  # Atualiza o "pai" do vizinho para o vértice atual
    
    # Se a busca terminar e não encontrar um caminho, imprime a mensagem de erro
    print("Não há caminho entre os vértices.")

def imprimir_caminho(pais, start, end):
    # Função auxiliar para reconstruir e imprimir o caminho entre 'start' e 'end'
    caminho = []
    atual = end
    # Começa do vértice final e segue os "pais" até chegar ao início
    while atual != -1:
        caminho.append(atual)  # Adiciona o vértice atual ao caminho
        atual = pais[atual]  # Move para o vértice pai
    
    # Inverte o caminho, pois ele foi construído do final para o início
    caminho.reverse()
    # Imprime o caminho no formato "vértice -> vértice"
    print(f"Caminho entre {start} e {end}: {' -> '.join(map(str, caminho))}")

def dfs_com_pilha(grafo, start):
    # Inicializa uma lista para marcar quais vértices já foram visitados
    visitados = [False] * grafo.vertices
    # Usa uma pilha para simular o comportamento da recursão no DFS
    pilha = [start]

    # Enquanto houver vértices na pilha, continua o processo
    while pilha:
        # Remove o próximo vértice da pilha para processar
        vertice = pilha.pop()

        # Se o vértice ainda não foi visitado, marca como visitado e imprime
        if not visitados[vertice]:
            print(vertice, end=" ")  # Imprime o vértice visitado
            visitados[vertice] = True  # Marca o vértice como visitado
            
            # Adiciona os vizinhos não visitados à pilha, em ordem reversa para simular DFS
            for vizinho in reversed(grafo.lista_adjacencia[vertice]):
                if not visitados[vizinho]:
                    pilha.append(vizinho)  # Adiciona o vizinho à pilha para processar mais tarde
