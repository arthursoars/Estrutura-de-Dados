from grafo import Grafo
from bfs_dfs import bfs, dfs_com_pilha

# Inicializar o grafo com os dados do arquivo 'meu_grafo.txt'
arquivo_grafo = "C:/Users/artur.DESKTOP-PQRS3PB/Downloads/ESTUDOS/UFPB/CIENCIA_DA_COMPUTAÇÃO/P3/ESTRUTRA DE DADOS/atividades-git/Estrutura-de-Dados/5 - Exercício - Grafo/meu_grafo.txt"
grafo = Grafo(0)  # Inicialmente vazio
grafo.carregar_grafo(arquivo_grafo)

# Executar BFS para encontrar o caminho entre dois vértices
vertice_inicial = 0
vertice_final = 4
print("Busca em Largura (BFS):")
bfs(grafo, vertice_inicial, vertice_final)

# Executar DFS usando pilha
print("\nBusca em Profundidade (DFS) com pilha:")
dfs_com_pilha(grafo, vertice_inicial)
