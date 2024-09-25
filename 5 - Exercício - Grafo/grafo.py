class Grafo:
    def __init__(self, vertices):
        # Inicializa o grafo com o número de vértices especificado
        self.vertices = vertices
        # Inicializa a matriz de adjacência com 0s (nenhuma conexão)
        self.matriz_adjacencia = [[0] * vertices for _ in range(vertices)]
        # Inicializa a lista de adjacência com listas vazias
        self.lista_adjacencia = [[] for _ in range(vertices)]

    def adicionar_aresta(self, u, v):
        # Adiciona uma aresta entre os vértices u e v
        # Atualiza a matriz de adjacência para indicar a conexão
        self.matriz_adjacencia[u][v] = 1  # Conexão de u para v
        self.matriz_adjacencia[v][u] = 1  # Conexão de v para u (não direcionado)
        
        # Atualiza a lista de adjacência para incluir os vértices conectados
        self.lista_adjacencia[u].append(v)  # Adiciona v à lista de u
        self.lista_adjacencia[v].append(u)  # Adiciona u à lista de v

    def carregar_grafo(self, arquivo):
        # Carrega o grafo a partir de um arquivo .txt
        with open(arquivo, 'r') as f:
            linhas = f.readlines()  # Lê todas as linhas do arquivo
            
            # A primeira linha contém o número de vértices
            vertices = int(linhas[0].strip())
            # Redefine o grafo com o número correto de vértices
            self.__init__(vertices)  # Re-inicializa a estrutura do grafo
            
            # Processa as arestas a partir das linhas restantes do arquivo
            for linha in linhas[1:]:
                u, v = map(int, linha.strip().split())  # Extrai os vértices da linha
                self.adicionar_aresta(u, v)  # Adiciona a aresta entre u e v
