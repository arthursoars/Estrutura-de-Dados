import locale

def selection_sort(vetor):
    n = len(vetor)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

def print_vetor(arr):
    print(" ".join(map(str, arr)))

def main():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    
    nomedoarquivo = input("Digite o nome do arquivo de entrada: ")

    try:
        with open(nomedoarquivo, "r") as arquivo:
            arr = [int(line.strip()) for line in arquivo]
    except FileNotFoundError:
        print(f"Não foi possível abrir o arquivo {nomedoarquivo}")
        return

    print("Escolha o algoritmo de ordenação:")
    print("1. Selection Sort")
    print("2. Insertion Sort")
    escolha = int(input("Digite sua escolha (1 ou 2): "))

    if escolha == 1:
        selection_sort(arr)
        print("Vetor ordenado com Selection Sort:")
    elif escolha == 2:
        insertion_sort(arr)
        print("Vetor ordenado com Insertion Sort:")
    else:
        print("Escolha inválida")
        return

    print_vetor(arr)

if __name__ == "__main__":
    main()
