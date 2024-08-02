# Jose Artur Soares Afreu - 20230146550
import locale
import time

# Função para ordenar o vetor usando o algoritmo Selection Sort
def selection_sort(vetor):
    n = len(vetor)
    for i in range(n - 1):
        min_idx = i
        # Encontrar o índice do menor elemento no restante do vetor
        for j in range(i + 1, n):
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        # Trocar o menor elemento encontrado com o elemento na posição i
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]

# Função para ordenar o vetor usando o algoritmo Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Mover os elementos do vetor que são maiores que a chave para uma posição à frente
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        # Inserir a chave na posição correta
        arr[j + 1] = key

# Função para imprimir os elementos do vetor
def print_vetor(arr):
    print(" ".join(map(str, arr)))

def main():
    # Configura a localidade para Português
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    # Solicita o nome do arquivo de entrada ao usuário
    nomedoarquivo = input("Digite o nome do arquivo de entrada: ")

    try:
        # Abre o arquivo e lê os números, armazenando-os no vetor
        with open(nomedoarquivo, "r") as arquivo:
            arr = [int(line.strip()) for line in arquivo]
    except FileNotFoundError:
        # Mensagem de erro se o arquivo não puder ser aberto
        print(f"Não foi possível abrir o arquivo {nomedoarquivo}")
        return

    # Solicita ao usuário para escolher o algoritmo de ordenação
    print("Escolha o algoritmo de ordenação:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    escolha = int(input("Digite sua escolha (1 ou 2): "))

    # Marcar o tempo de início
    inicio = time.time()
    
    if escolha == 1:
        # Ordena o vetor usando Selection Sort
        selection_sort(arr)
        print("Vetor ordenado com Selection Sort:")
    elif escolha == 2:
        # Ordena o vetor usando Insertion Sort
        insertion_sort(arr)
        print("Vetor ordenado com Insertion Sort:")
    else:
        # Mensagem de erro para escolha inválida
        print("Escolha inválida")
        return
    
    # Marcar o tempo de fim
    fim = time.time()
    
    # Imprime o vetor ordenado
    print_vetor(arr)
    # Exibe o tempo de execução do algoritmo
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")

if __name__ == "__main__":
    main()
